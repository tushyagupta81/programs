const std = @import("std");
const outw = std.io.getStdOut().writer();
const RndGen = std.Random.DefaultPrng;

pub fn main() !void {
    const file = try std.fs.cwd().openFile("src/words.txt", .{});
    defer file.close();

    const content = try file.readToEndAlloc(std.heap.page_allocator, std.math.maxInt(usize));
    var words = std.mem.splitSequence(u8, content, "\n");

    var seed: u64 = undefined;
    try std.posix.getrandom(std.mem.asBytes(&seed));

    var rnd = RndGen.init(seed);
    const randn = rnd.random().uintAtMost(u32, 2637);

    var i: usize = 0;
    const answer = while (words.next()) |word| : (i += 1) {
        if (randn == i) {
            break word;
        }
    } else "tushy";

    const stdin = std.io.getStdIn().reader();
    var counter: u8 = 0;

    var win = false;
    while (true) {
        if (counter >= 5) {
            try outw.print("The word was '{s}'\n", .{answer});
            try outw.print("You Lose!\n", .{});
            std.process.exit(0);
        }

        try outw.print("guess: ", .{});
        const guess = try stdin.readUntilDelimiterAlloc(std.heap.page_allocator, '\n', 8192);

        if (guess.len != 5) {
            try outw.print("Guess must be 5 long\n\n", .{});
            continue;
        } else {
            counter += 1;
        }

        win = true;
        for (guess, 0..) |letter, index| {
            if (letter == answer[index]) {
                try outw.print("*{c} ", .{letter});
            } else {
                try outw.print("!{c} ", .{letter});
                win = false;
            }
        }

        try outw.print("\n", .{});

        if (win) {
            try outw.print("The word was '{s}'\n", .{answer});
            try outw.print("You Win!\n", .{});
            std.process.exit(0);
        }

        try outw.print("\n", .{});
    }
}
