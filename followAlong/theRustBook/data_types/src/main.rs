fn plus_one(mut x: i32) -> i32 {
    x + 1; // This is a statement
    x + 1 // This is a expression ie it returns a val
}

fn main() {
    println!("{}", plus_one(4));
    let t: (u8, f32, i32) = (1, 3.43, -2);
    println!("first = {}", t.0);
    println!("second = {}", t.1);
    println!("third = {}", t.2);

    let arr: [u32; 5] = [1, 2, 3, 4, 5];
    let mut i = 0;
    loop {
        println!("{}", arr[i]);
        i += 1;
        if i == 5 {
            break;
        }
    }
    let arr = [5; 10];
    let mut i = 0;
    loop {
        println!("{}", arr[i]);
        i += 1;
        if i == 10 {
            break;
        }
    }
}
