#[derive(Debug)]
enum IpAddr {
    V4(u32, u32, u32, u32),
    V6(String),
}

fn main() {
    let four = IpAddr::V4(127, 0, 0, 1);
    let six = IpAddr::V6(String::from("::1"));
    dbg!(&four);
    dbg!(&six);
}
