const std = @import("std");

const Node = struct {
    const Self = @This();

    val: u32,
    next: ?*Node = null,
};

const stdout = std.io.getStdOut().writer();

pub fn main() !void {
    var head: ?*Node = undefined;
    var n1 = Node{
        .val = 1,
    };
    var n2 = Node{
        .val = 2,
    };
    n2.val += 1;
    n1.next = &n2;

    head = &n1;
    while (head != null) : (head = head.?.next) {
        try stdout.print("{}\n", .{head.?.val});
    }

    try stdout.print("n1 {} -> n2 {}", .{ n1.val, n1.next.?.*.val });
}
