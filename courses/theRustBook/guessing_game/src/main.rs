use rand::Rng;
use std::cmp::Ordering;
use std::io;
use std::io::Write;

fn main() {
    println!("Guess the number!");

    let secret_num = rand::thread_rng().gen_range(1..=100);
    // println!("The secret number is: {secret_num}");

    loop {
        print!("Enter a number: ");
        io::stdout().flush().unwrap();

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line!!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        // println!("You guessed: {}", guess);

        match guess.cmp(&secret_num) {
            Ordering::Less => println!("Your guess is lower than secret number."),
            Ordering::Greater => println!("Your guess is higher than secret number."),
            Ordering::Equal => {
                println!("Your guess is correct!");
                break;
            }
        }
    }
}
