mod scanner;
mod expr;
mod parser;
use parser::Parser;

use crate::scanner::*;

use std::env;
use std::error::Error;
use std::fs;
use std::io;
use std::io::Write;
use std::process::exit;

fn run_file(path: &str) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(path)?;
    //println!("{}", contents);
    run(&contents)?;
    Ok(())
}

fn run(contents: &str) -> Result<(), Box<dyn Error>> {
    let mut scanner = Scanner::new(contents);
    let tokens = scanner.scan_tokens()?;

    let mut parser = Parser::new(tokens);
    let parser_expr = parser.parse()?;
    let string_expr = parser_expr.to_string();
    println!("{:?}",parser_expr);
    println!("{}",string_expr);
    Ok(())
}

fn run_promt() -> Result<(), Box<dyn Error>> {
    loop {
        print!("> ");
        io::stdout().flush().unwrap();
        let stdin = io::stdin();
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        if buffer.trim() == "exit" || buffer.trim() == "" {
            break;
        }
        match run(&buffer) {
            Ok(_) => (),
            Err(e) => println!("{}", e),
        }
        println!("You typed: {}", buffer);
    }
    Ok(())
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() == 1 {
        match run_promt() {
            Err(e) => {
                println!("Error: {}", e);
                exit(1);
            }
            _ => (),
        }
    } else if args.len() == 2 {
        match run_file(&args[1]) {
            Err(e) => {
                println!("Error: {}", e);
                exit(1);
            }
            _ => (),
        }
    } else if args.len() > 2 {
        println!("Usage: script");
        println!("\tOR");
        println!("Usage: script [file path]");
        exit(64);
    }
    //dbg!(args);
}
