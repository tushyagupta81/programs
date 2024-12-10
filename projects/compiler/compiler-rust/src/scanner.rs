use crate::TokenType::*;
use core::fmt;
use std::error::Error;
use std::fmt::format;
use std::string::String;

pub struct Scanner {
    source: String,
    tokens: Vec<Token>,
    start: usize,
    current: usize,
    line: usize,
}

fn is_digit(ch: char) -> bool {
    ch >= '0' && ch <= '9'
}

impl Scanner {
    pub fn new(source: &str) -> Self {
        Self {
            source: source.to_string(),
            tokens: vec![],
            start: 0,
            current: 0,
            line: 1,
        }
    }
    pub fn scan_tokens(self: &mut Self) -> Result<Vec<Token>, Box<dyn Error>> {
        let mut errors = vec![];
        while !self.is_at_end() {
            self.start = self.current;
            // scann tokens in line
            match self.scan_token() {
                Err(e) => errors.push(e),
                _ => (),
            }
        }
        // After scanning everything push a EOF Token at the end
        self.tokens.push(Token {
            token_type: TokenType::Eof,
            lexeme: "".to_string(),
            literal: None,
            line_number: self.line,
        });

        // If any error print all of them together
        if errors.len() > 0 {
            let mut joined = "".to_string();
            errors.iter().for_each(|error| {
                joined.push_str(format!("{}", error).as_str());
                joined.push_str("\n");
            });
            return Err(joined.into());
        }
        Ok(self.tokens.clone())
    }

    // Check if we have exceded the length of the document/source
    fn is_at_end(self: &Self) -> bool {
        self.current >= self.source.len()
    }

    fn scan_token(self: &mut Self) -> Result<(), Box<dyn Error>> {
        let c = self.advance();

        match c {
            '(' => self.add_token(LeftParen),
            ')' => self.add_token(RightParen),
            '{' => self.add_token(LeftBrace),
            '}' => self.add_token(RightBrace),
            ',' => self.add_token(Comma),
            '.' => self.add_token(Dot),
            '+' => self.add_token(Plus),
            '-' => self.add_token(Minus),
            ';' => self.add_token(Semicolon),
            '*' => self.add_token(Star),

            '!' => {
                let token = if self.char_match('=') {
                    BangEqual
                } else {
                    Bang
                };
                self.add_token(token);
            }
            '=' => {
                let token = if self.char_match('=') {
                    EqualEqual
                } else {
                    Equal
                };
                self.add_token(token);
            }
            '>' => {
                let token = if self.char_match('=') {
                    GreaterEqual
                } else {
                    Greater
                };
                self.add_token(token);
            }
            '<' => {
                let token = if self.char_match('=') {
                    LessEqual
                } else {
                    Less
                };
                self.add_token(token);
            }

            '/' => {
                if self.char_match('/') {
                    loop {
                        if self.peek() == '\n' || self.is_at_end() {
                            break;
                        }
                        self.advance();
                    }
                } else {
                    self.add_token(Slash);
                };
            }

            '"' => match self.string_literal() {
                Err(e) => return Err(e),
                _ => (),
            },

            ' ' | '\r' | '\t' => (),
            '\n' => self.line += 1,

            c => {
                if is_digit(c) {
                    match self.number() {
                        Err(e) => return Err(e),
                        _ => (),
                    }
                } else {
                    return Err(format!("Unrecognised char {} at line {}", c, self.line).into());
                }
            } 
        }
        Ok(())
    }

    fn number(self: &mut Self) -> Result<(),Box<dyn Error>> {
        while is_digit(self.peek()) {
            self.advance();
        }

        if self.peek() == '.' && is_digit(self.peek_next()) {
            self.advance();
            while is_digit(self.peek()) {
                self.advance();
            }
        }

        let s = &self.source.as_str()[self.start..self.current];
        match s.parse::<f64>() {
            Ok(v) => {
                self.add_token_lit(Number, Some(LiteralValue::FloatValue(v)));
            },
            Err(_) => return Err(format!("Failed to parse number at line {}",self.line).into()),
        }
        Ok(())
    }

    fn char_match(self: &mut Self, c: char) -> bool {
        if self.is_at_end() {
            return false;
        }
        if self.source.as_bytes()[self.current] as char != c {
            false
        } else {
            self.current += 1;
            true
        }
    }

    fn string_literal(self: &mut Self) -> Result<(), Box<dyn Error>> {
        while !self.is_at_end() && self.peek() != '"' {
            if self.peek() == '\n' {
                self.line += 1;
            }
            self.advance();
        }
        self.advance();
        if self.is_at_end() {
            return Err("String is not terminated".into());
        }
        let literal = &self.source.as_str()[self.start + 1..self.current - 1];
        let literal = LiteralValue::StringValue(literal.to_string());
        self.add_token_lit(String_, Some(literal));
        Ok(())
    }

    fn peek(self: &Self) -> char {
        if self.is_at_end() {
            return '\0';
        }
        self.source.as_bytes()[self.current] as char
    }

    fn peek_next(self: &Self) -> char {
        if self.current + 1 > self.source.len() {
            return '\0';
        } else {
            self.source.as_bytes()[self.current + 1] as char
        }
    }

    fn add_token(self: &mut Self, token_type: TokenType) {
        self.add_token_lit(token_type, None);
    }

    // Add a token to the struct tokens vector
    fn add_token_lit(self: &mut Self, token_type: TokenType, literal: Option<LiteralValue>) {
        let text = &self.source.as_str()[self.start..self.current];
        self.tokens.push(Token {
            token_type,
            lexeme: text.to_string(),
            literal,
            line_number: self.line,
        })
    }

    // return current char and increment the pointer by 1
    fn advance(self: &mut Self) -> char {
        if self.is_at_end() {
            return '\0';
        }
        let c = self.source.as_bytes()[self.current];
        self.current += 1;
        c as char
    }
}

#[derive(Debug, Clone, PartialEq)]
pub enum TokenType {
    LeftParen,
    RightParen,
    LeftBrace,
    RightBrace,

    Comma,
    Dot,
    Plus,
    Minus,
    Semicolon,
    Slash,
    Star,

    Bang,
    BangEqual,
    Greater,
    GreaterEqual,
    Less,
    LessEqual,
    Equal,
    EqualEqual,

    Identifier,
    String_,
    Number,

    And,
    Or,
    True,
    False,
    Class,
    If,
    Else,
    Func,
    For,
    While,
    Nil,
    Print,
    Return,
    Super,
    This,
    Var,

    Eof,
}

impl std::fmt::Display for TokenType {
    fn fmt(&self, f: &mut fmt::Formatter) -> std::fmt::Result {
        write!(f, "{:?}", self)
    }
}

#[derive(Debug, Clone)]
pub enum LiteralValue {
    IntValue(i64),
    FloatValue(f64),
    StringValue(String),
    IdentifierValue(String),
}

#[derive(Debug, Clone)]
pub struct Token {
    token_type: TokenType,
    lexeme: String,
    literal: Option<LiteralValue>,
    line_number: usize,
}

impl Token {
    pub fn new(
        token_type: TokenType,
        lexeme: String,
        literal: LiteralValue,
        line_number: usize,
    ) -> Self {
        Self {
            token_type,
            lexeme,
            literal: Some(literal),
            line_number,
        }
    }

    pub fn to_string(self: &Self) -> String {
        format!("{} {} {:?}", self.token_type, self.lexeme, self.literal)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn handle_single_char_tokens() -> Result<(), Box<dyn Error>> {
        let source = "(){}=/-+*.,;";
        let mut scanner = Scanner::new(source);
        scanner.scan_tokens()?;

        assert_eq!(scanner.tokens.len(), source.len() + 1);
        assert_eq!(scanner.tokens[0].token_type, LeftParen);
        assert_eq!(scanner.tokens[1].token_type, RightParen);
        assert_eq!(scanner.tokens[2].token_type, LeftBrace);
        assert_eq!(scanner.tokens[3].token_type, RightBrace);
        assert_eq!(scanner.tokens[4].token_type, Equal);
        assert_eq!(scanner.tokens[5].token_type, Slash);
        assert_eq!(scanner.tokens[6].token_type, Minus);
        assert_eq!(scanner.tokens[7].token_type, Plus);
        assert_eq!(scanner.tokens[8].token_type, Star);
        assert_eq!(scanner.tokens[9].token_type, Dot);
        assert_eq!(scanner.tokens[10].token_type, Comma);
        assert_eq!(scanner.tokens[11].token_type, Semicolon);
        assert_eq!(scanner.tokens[12].token_type, Eof);

        Ok(())
    }

    #[test]
    fn handle_double_char_tokens() -> Result<(), Box<dyn Error>> {
        let source = "== >= <= != // this is a comment";
        let mut scanner = Scanner::new(source);
        scanner.scan_tokens()?;

        assert_eq!(scanner.tokens.len(), 5);
        assert_eq!(scanner.tokens[0].token_type, EqualEqual);
        assert_eq!(scanner.tokens[1].token_type, GreaterEqual);
        assert_eq!(scanner.tokens[2].token_type, LessEqual);
        assert_eq!(scanner.tokens[3].token_type, BangEqual);
        assert_eq!(scanner.tokens[4].token_type, Eof);

        Ok(())
    }

    #[test]
    fn check_is_digit() -> Result<(), Box<dyn Error>> {
        assert_eq!(is_digit('0'), true);
        assert_eq!(is_digit('1'), true);
        assert_eq!(is_digit('2'), true);
        assert_eq!(is_digit('3'), true);
        assert_eq!(is_digit('4'), true);
        assert_eq!(is_digit('5'), true);
        assert_eq!(is_digit('6'), true);
        assert_eq!(is_digit('7'), true);
        assert_eq!(is_digit('8'), true);
        assert_eq!(is_digit('9'), true);
        assert_eq!(is_digit('i'), false);
        Ok(())
    }
}
