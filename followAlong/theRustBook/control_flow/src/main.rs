use std::io;
use std::io::Write;

fn main() {
    let mut x = String::new();
    print!("Enter a number: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut x).expect("Input a number.");
    let x: i32 = x.trim().parse().expect("Input a number.");

    if x > 3 {
        println!("{} greater than 3", x);
    } else {
        println!("{} less than 3", x);
    }

    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
