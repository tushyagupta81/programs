use std::error::Error;

use crate::{scanner, TokenType};

use super::scanner::Token;

#[derive(Clone, Debug, PartialEq)]
pub enum LiteralValue {
    Number(f32),
    StringValue(String),
    True,
    False,
    Nil,
}

fn unwrap_as_f32(literal: Option<scanner::LiteralValue>) -> f32 {
    match literal {
        Some(scanner::LiteralValue::IntValue(x)) => x as f32,
        Some(scanner::LiteralValue::FloatValue(x)) => x as f32,
        _ => panic!("Couldnt unwrap as f32"),
    }
}

fn unwrap_as_string(literal: Option<scanner::LiteralValue>) -> String {
    match literal {
        Some(scanner::LiteralValue::StringValue(s)) => s.clone(),
        Some(scanner::LiteralValue::IdentifierValue(s)) => s.clone(),
        _ => panic!("Couldnt unwrap to string"),
    }
}

impl LiteralValue {
    pub fn to_string(&self) -> String {
        match self {
            LiteralValue::Number(n) => n.to_string(),
            LiteralValue::StringValue(s) => s.clone(),
            LiteralValue::True => "true".to_string(),
            LiteralValue::False => "false".to_string(),
            LiteralValue::Nil => "nil".to_string(),
        }
    }

    pub fn from_token(token: &Token) -> Self {
        match token.token_type {
            TokenType::Number => Self::Number(unwrap_as_f32(token.literal.clone())),
            TokenType::String_ => Self::StringValue(unwrap_as_string(token.literal.clone())),
            TokenType::True => Self::True,
            TokenType::False => Self::False,
            TokenType::Nil => Self::Nil,
            _ => panic!("Cannot create literal from {:?}", token),
        }
    }

    pub fn is_falsy(&self) -> LiteralValue {
        match self {
            LiteralValue::Number(e) => {
                if *e == 0. {
                    LiteralValue::True
                } else {
                    LiteralValue::False
                }
            }
            LiteralValue::StringValue(s) => {
                if s.len() == 0 {
                    LiteralValue::True
                } else {
                    LiteralValue::False
                }
            }
            LiteralValue::False => LiteralValue::True,
            LiteralValue::True => LiteralValue::False,
            LiteralValue::Nil => LiteralValue::True,
        }
    }

    pub fn compare(&self, right: &Self) -> bool {
        match self {
            LiteralValue::Nil => {
                if *right == LiteralValue::Nil {
                    return true;
                } else {
                    return false;
                }
            }
            LiteralValue::True => {
                if *right == LiteralValue::True {
                    return true;
                } else {
                    return false;
                }
            }
            LiteralValue::False => {
                if *right == LiteralValue::False {
                    return true;
                } else {
                    return false;
                }
            }
            LiteralValue::Number(e) => {
                if *right == LiteralValue::Number(*e) {
                    return true;
                } else {
                    return false;
                }
            }
            LiteralValue::StringValue(s) => {
                if *right == LiteralValue::StringValue(s.clone()) {
                    return true;
                } else {
                    return false;
                }
            }
        }
    }
}

#[derive(Clone, Debug)]
pub enum Expr {
    Binary {
        left: Box<Expr>,
        operator: Token,
        right: Box<Expr>,
    },
    Grouping {
        expression: Box<Expr>,
    },
    Literal {
        literal: LiteralValue,
    },
    Unary {
        operator: Token,
        right: Box<Expr>,
    },
}

impl Expr {
    pub fn to_string(&self) -> String {
        match self {
            Expr::Binary {
                left,
                operator,
                right,
            } => {
                let left_str = (*left).to_string();
                let op = operator.lexeme.clone();
                let right_str = (*right).to_string();
                format!("({} {} {})", op, left_str, right_str)
            }
            Expr::Grouping { expression } => {
                format!("(group {})", (*expression).to_string())
            }
            Expr::Literal { literal } => literal.to_string(),
            Expr::Unary { operator, right } => {
                let op_str = operator.lexeme.clone();
                let right_str = (*right).to_string();
                format!("({} {})", op_str, right_str)
            }
        }
    }

    pub fn evaluvate(&self) -> Result<LiteralValue, Box<dyn Error>> {
        let res = match self {
            Expr::Literal { literal } => literal.clone(),
            Expr::Grouping { expression } => expression.evaluvate()?,
            Expr::Unary { operator, right } => {
                let right = &right.evaluvate()?;
                match (right, &operator.token_type) {
                    (LiteralValue::Number(n), TokenType::Minus) => LiteralValue::Number(-n),
                    (any, TokenType::Bang) => any.is_falsy(),
                    _ => {
                        return Err(format!(
                            "{:?} Not not a valif Unary operator on {:?}",
                            &operator.token_type, right
                        )
                        .into())
                    }
                }
            }
            Expr::Binary {
                left,
                operator,
                right,
            } => {
                let left = &left.evaluvate()?;
                let right = &right.evaluvate()?;
                match (left, right, &(*operator).token_type) {
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::Greater) => {
                        if a > b {
                            LiteralValue::True
                        } else {
                            LiteralValue::False
                        }
                    }
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::GreaterEqual) => {
                        if a >= b {
                            LiteralValue::True
                        } else {
                            LiteralValue::False
                        }
                    }
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::Less) => {
                        if a < b {
                            LiteralValue::True
                        } else {
                            LiteralValue::False
                        }
                    }
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::LessEqual) => {
                        if a <= b {
                            LiteralValue::True
                        } else {
                            LiteralValue::False
                        }
                    }
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::Star) => {
                        LiteralValue::Number(a * b)
                    }
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::Slash) => {
                        LiteralValue::Number(a / b)
                    }
                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::Minus) => {
                        LiteralValue::Number(a - b)
                    }

                    (LiteralValue::Number(a), LiteralValue::Number(b), TokenType::Plus) => {
                        LiteralValue::Number(a + b)
                    }
                    (
                        LiteralValue::StringValue(a),
                        LiteralValue::StringValue(b),
                        TokenType::Plus,
                    ) => LiteralValue::StringValue(format!("{}{}", a, b)),

                    (left, right, TokenType::EqualEqual) => {
                        if left.compare(right) {
                            LiteralValue::True
                        } else {
                            LiteralValue::False
                        }
                    }
                    (left, right, TokenType::BangEqual) => {
                        if left.compare(right) {
                            LiteralValue::False
                        } else {
                            LiteralValue::True
                        }
                    }
                    _ => {
                        return Err(format!(
                            "{:?} Not implemented on '{:?}' and '{:?}'",
                            &operator.token_type, left, right
                        )
                        .into())
                    }
                }
            }
        };
        Ok(res)
    }

    pub fn print(&self) {
        println!("{}", self.to_string());
    }
}

#[cfg(test)]
mod tests {
    use std::usize;

    use super::*;
    use crate::scanner::TokenType;

    #[test]
    fn pretty_print_ast() {
        let minus_token = Token {
            token_type: TokenType::Minus,
            lexeme: "-".to_string(),
            literal: None,
            line_number: 1 as usize,
        };

        let onetwothree = Box::new(Expr::Literal {
            literal: LiteralValue::Number(123.0),
        });
        let multi = Token {
            token_type: TokenType::Star,
            lexeme: "*".to_string(),
            literal: None,
            line_number: 1 as usize,
        };
        let group = Box::new(Expr::Grouping {
            expression: Box::new(Expr::Literal {
                literal: LiteralValue::Number(45.67),
            }),
        });

        let ast = Expr::Binary {
            left: Box::new(Expr::Unary {
                operator: minus_token,
                right: onetwothree,
            }),
            operator: multi,
            right: group,
        };

        ast.print();
        assert_eq!(ast.to_string(), "(* (- 123) (group 45.67))".to_string());
    }
}
