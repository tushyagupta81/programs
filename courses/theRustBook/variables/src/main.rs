fn main() {
    let x = 5e+2;
    println!("{x}");
    {
        let x: f64 = 22.0 / 7.0;
        println!("{x}");
        let x: f32 = x as f32;
        println!("{x}");
    }
}
