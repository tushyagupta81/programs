use std::error::Error;

pub struct Scanner {}

impl Scanner {
    pub fn new(_source: &str) -> Self {
        Self {}
    }
    pub fn scan_tokens(self: &Self) -> Result<Vec<Token>, Box<dyn Error>> {
        todo!();
    }
}

#[derive(Debug)]
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
    Start,

    Bang,
    BangEqual,
    Greater,
    GreaterEqual,
    Less,
    LessEqual,

    Identifier,
    String,
    Number,

    And,
    Class,
    Else,
    False,
    Fun,
    For,
    If,
    Nil,
    Or,
    Print,
    Return,
    Super,
    This,
    True,
    Var,
    While,

    EOF,
}

#[derive(Debug)]
pub enum LiteralValue {
    IntValue(i64),
    FloatValue(f64),
    StringValue(String),
    IdentifierValue(String),
}

#[derive(Debug)]
pub struct Token {
    token_type: TokenType,
    lexeme: String,
    literal: LiteralValue,
    line_number: u64,
}

impl Token {
    pub fn new(
        token_type:TokenType,
        lexeme:String,
        literal:LiteralValue,
        line_number:u64,
    ) -> Self {
        Self {
            token_type,
            lexeme,
            literal,
            line_number,
        }
    }
}
