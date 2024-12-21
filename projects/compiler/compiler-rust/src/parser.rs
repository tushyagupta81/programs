use crate::expr::*;
use crate::scanner::Token;
use crate::scanner::TokenType::*;
use crate::TokenType;

pub struct Parser {
    tokens: Vec<Token>,
    current: usize,
}

impl Parser {
    pub fn new(tokens: Vec<Token>) -> Self {
        Self { tokens, current: 0 }
    }

    pub fn parse(&mut self) -> Result<Expr,String> {
        self.expression()
    }

    fn expression(&mut self) -> Result<Expr, String> {
        self.equality()
    }

    fn equality(&mut self) -> Result<Expr, String> {
        let mut lhs_expr = self.comparision()?;
        while self.match_tokens(vec![BangEqual, EqualEqual]) {
            let op = self.previous().clone();
            let rhs_expr = self.comparision()?;
            lhs_expr = Expr::Binary {
                left: Box::from(lhs_expr),
                opertaor: op,
                right: Box::from(rhs_expr),
            };
        }
        Ok(lhs_expr)
    }

    fn comparision(&mut self) -> Result<Expr, String> {
        let mut lhs_expr = self.term()?;

        while self.match_tokens(vec![Greater, GreaterEqual, LessEqual, Less]) {
            let op = self.previous().clone();
            let rhs_expr = self.term()?;
            lhs_expr = Expr::Binary {
                left: Box::from(lhs_expr),
                opertaor: op,
                right: Box::from(rhs_expr),
            }
        }

        Ok(lhs_expr)
    }

    fn term(&mut self) -> Result<Expr, String> {
        let mut lhs_expr = self.factor()?;

        while self.match_tokens(vec![Minus, Plus]) {
            let op = self.previous().clone();
            let rhs_expr = self.factor()?;
            lhs_expr = Expr::Binary {
                left: Box::from(lhs_expr),
                opertaor: op,
                right: Box::from(rhs_expr),
            }
        }

        Ok(lhs_expr)
    }

    fn factor(&mut self) -> Result<Expr, String> {
        let mut lhs_expr = self.unary()?;

        while self.match_tokens(vec![Slash, Star]) {
            let op = self.previous().clone();
            let rhs_expr = self.unary()?;
            lhs_expr = Expr::Binary {
                left: Box::from(lhs_expr),
                opertaor: op,
                right: Box::from(rhs_expr),
            }
        }

        Ok(lhs_expr)
    }

    fn unary(&mut self) -> Result<Expr, String> {
        if self.match_tokens(vec![Minus, Bang]) {
            let op = self.previous().clone();
            let rhs_expr = self.unary()?;
            return Ok(Expr::Unary {
                operator: op,
                right: Box::from(rhs_expr),
            });
        }
        self.primary()
    }

    fn primary(&mut self) -> Result<Expr, String> {
        let token = self.peek();

        let result;
        match token.token_type {
            LeftParen => {
                self.advance();
                let expr = self.expression()?;
                self.consume(RightParen, "Expected ')'")?;
                result = Expr::Grouping {
                    expression: Box::from(expr),
                };
            }
            Number | String_ | True | False | Nil => {
                result = Expr::Literal {
                    literal: LiteralValue::from_token(token),
                };
            }
            _ => return Err(format!("{:?} is not a primary", self.peek())),
        }
        self.advance();
        return Ok(result);
    }

    fn consume(&mut self, token_type: TokenType, msg: &str) -> Result<(), String> {
        let token = self.peek();
        if token.token_type == token_type {
            self.advance();
            Ok(())
        } else {
            Err(msg.to_string())
        }
    }

    fn previous(&mut self) -> &Token {
        &self.tokens[self.current - 1]
    }

    fn is_at_end(&mut self) -> bool {
        self.tokens[self.current].token_type == Eof
    }

    fn peek(&mut self) -> &Token {
        &self.tokens[self.current]
    }

    fn match_token(&mut self, token: TokenType) -> bool {
        if self.is_at_end() {
            return false;
        } else {
            if self.peek().token_type == token {
                self.advance();
                return true;
            } else {
                return false;
            }
        }
    }

    fn match_tokens(&mut self, token_types: Vec<TokenType>) -> bool {
        for token_type in token_types {
            if self.match_token(token_type) {
                return true;
            }
        }
        false
    }

    fn advance(&mut self) -> &Token {
        if !self.is_at_end() {
            self.current += 1;
        }
        self.previous()
    }

    fn synchronize(&mut self) {
        self.advance();

        while !self.is_at_end() {
            if self.peek().token_type == Eof {
                return;
            }
            match self.peek().token_type {
                Class | Func | Var | For | If | While | Print | Return => return,
                _ => (),
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use std::error::Error;

    use super::*;
    use crate::{scanner::LiteralValue, Scanner};
    #[test]
    fn test_addition() -> Result<(), Box<dyn Error>> {
        let one = Token {
            token_type: Number,
            lexeme: "1".to_string(),
            literal: Some(LiteralValue::IntValue(1)),
            line_number: 0,
        };
        let plus = Token {
            token_type: Plus,
            lexeme: "+".to_string(),
            literal: None,
            line_number: 0,
        };
        let two = Token {
            token_type: Number,
            lexeme: "2".to_string(),
            literal: Some(LiteralValue::IntValue(2)),
            line_number: 0,
        };
        let semicolon = Token {
            token_type: Semicolon,
            lexeme: ";".to_string(),
            literal: None,
            line_number: 0,
        };
        let tokens = vec![one, plus, two, semicolon];

        let mut parser = Parser::new(tokens);
        let parsed_expr = parser.parse()?;
        let string_expr = parsed_expr.to_string();

        assert_eq!(string_expr, "(+ 1 2)");
        Ok(())
    }

    #[test]
    fn test_comparison() -> Result<(), Box<dyn Error>> {
        let source = "1+2 == 3+4";
        let mut scanner = Scanner::new(source);
        let tokens = scanner.scan_tokens().unwrap();

        let mut parser = Parser::new(tokens);
        let parsed_expr = parser.parse()?;
        let string_expr = parsed_expr.to_string();

        assert_eq!(string_expr, "(== (+ 1 2) (+ 3 4))");
        Ok(())
    }

    #[test]
    fn test_factor() -> Result<(), Box<dyn Error>> {
        let source = "3-4*2;";
        let mut scanner = Scanner::new(source);
        let tokens = scanner.scan_tokens().unwrap();

        let mut parser = Parser::new(tokens);
        let parsed_expr = parser.parse()?;
        let string_expr = parsed_expr.to_string();

        assert_eq!(string_expr, "(- 3 (* 4 2))");

        Ok(())
    }

    #[test]
    fn test_eq_with_paren() -> Result<(), Box<dyn Error>> {
        let source = "1 == (2+2)";
        let mut scanner = Scanner::new(source);
        let tokens = scanner.scan_tokens().unwrap();

        let mut parser = Parser::new(tokens);
        let parsed_expr = parser.parse()?;
        let string_expr = parsed_expr.to_string();

        assert_eq!(string_expr, "(== 1 (group (+ 2 2)))");

        Ok(())
    }
}
