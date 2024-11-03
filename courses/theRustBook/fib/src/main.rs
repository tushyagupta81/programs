use std::io;
use std::io::Write;

fn main() {
    let mut n = String::new();
    print!("Enter a number: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut n).expect("Failed to read line.");
    let n: i32 = n.trim().parse().expect("Please enter a number.");

    let mut a = 0;
    let mut b = 1;
    print!("{a} ");
    for _i in 1..n {
        print!("{b} ");
        let temp = a;
        a = b;
        b = temp + b;
    }
}
