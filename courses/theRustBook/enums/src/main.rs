enum Coin {
    Penny,
    Nickel,
    Dime,
}
fn val_cents(coin: &Coin) -> u32 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
    }
}
fn main() {
    let p = Coin::Penny;
    let n = Coin::Nickel;
    let d = Coin::Dime;
    println!("{}", val_cents(&p));
    println!("{}", val_cents(&n));
    println!("{}", val_cents(&d));
}
