fn main() {
    let config_max = Some(3u8);
    if let Some(max) = config_max {
        println!("Max is configed to {max}");
    } else {
        println!("Not configed");
    }
}
