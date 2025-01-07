const std = @import("std");

const Node = struct {
    val: i32,
    next: ?*Node = null,

    pub fn add_next(node: *Node, nn: *Node) void {
        node.next = nn;
    }
};

pub fn main() void {
    var root = Node{
        .val = 0,
    };
    var nn = Node{
        .val = 1,
    };
    root.add_next(&nn);
    std.debug.print("{d} {any}", .{ root.val, root.next.?.val });
}
