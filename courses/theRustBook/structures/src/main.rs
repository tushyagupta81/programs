#[derive(Debug)]
struct User {
    username: String,
    age: u8,
    phone: u64,
}

#[derive(Debug)]
struct Rect {
    width: u32,
    length: u32,
}

impl Rect {
    fn area(&self) -> u32 {
        self.width * self.length
    }
    fn can_hold(&self, rect: &Rect) -> bool {
        if rect.width <= self.width && rect.length <= self.length {
            return true;
        } else {
            return false;
        }
    }
    fn sqaure(s: u32) -> Self {
        Rect {
            width: s,
            length: s,
        }
    }
}

fn create_user(username: String, age: u8, phone: u64) -> User {
    User {
        username,
        age,
        phone,
    }
}

fn main() {
    let tu = create_user(String::from("Tushya"), 20, 9877627732);
    let user2 = User {
        username: String::from("New Tushya"),
        ..tu
    };
    println!("{} {} {}", tu.username, tu.age, tu.phone);
    println!("{} {} {}", user2.username, user2.age, user2.phone);
    println!("{tu:#?}");
    dbg!(&tu);

    let rect1 = Rect {
        width: 32,
        length: 2,
    };
    let rect2 = Rect {
        width: 16,
        length: 4,
    };
    let rect3 = Rect {
        width: 4,
        length: 2,
    };
    println!("Area of rect = {}", rect1.area());
    println!("rect1 can hold rect2 -> {}", rect1.can_hold(&rect2));
    println!("rect2 can hold rect3 -> {}", rect2.can_hold(&rect3));

    let sq = Rect::sqaure(5);
    dbg!(&sq);
}
