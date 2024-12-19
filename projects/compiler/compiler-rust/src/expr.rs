use super::scanner::Token;

pub enum LiteralValue {
    Number(f32),
    StringValue(String),
    True,
    False,
    Nil,
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
}

pub enum Expr {
    Binary {
        left: Box<Expr>,
        opertaor: Token,
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
                opertaor,
                right,
            } => {
                let left_str = (*left).to_string();
                let op = opertaor.lexeme.clone();
                let right_str = (*right).to_string();
                format!("({} {} {})", op, left_str, right_str)
            }
            Expr::Grouping { expression } => {
                format!("(group {})", (*expression).to_string())
            }
            Expr::Literal { literal } => {
                format!("{}", literal.to_string())
            }
            Expr::Unary { operator, right } => {
                let op_str = operator.lexeme.clone();
                let right_str = (*right).to_string();
                format!("({} {})", op_str, right_str)
            }
        }
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
            opertaor: multi,
            right: group,
        };

        assert_eq!(ast.to_string(), "(* (- 123) (group 45.67))".to_string());
    }
}
