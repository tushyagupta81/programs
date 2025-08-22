graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}


def dfs(graph, start, goal):
    visited = set()
    stack = [start]

    while len(stack) != 0:
        vertex = stack.pop()
        if vertex == goal:
            print(f"{vertex} > ", end="")
            return
        if vertex not in visited:
            print(f"{vertex} > ", end="")
            visited.add(vertex)

            for node in graph[vertex]:
                if node not in visited:
                    stack.append(node)


dfs(graph, "A", "F")
print()
#
# graph = {
#     "A": [("B", 2), ("C", 2)],
#     "B": [("D", 2), ("E", 2)],
#     "C": [("F", 2), ("G", 2)],
#     "D": [],
#     "E": [],
#     "F": [],
#     "G": [],
# }
# path = []
#
#
# def recc_cost(graph, visited, curr, goal, cost):
#     path.append(curr)
#     visited.add(curr)
#     if curr == goal:
#         return cost
#     for node in graph[curr]:
#         if node[0] not in visited:
#             v = recc_cost(graph, visited, node[0], goal, cost + node[1])
#             if v != -1:
#                 return v
#     path.pop()
#     return -1
#
#
# inp = input("Entry: ").upper()
# out = input("Goal: ").upper()
# print(recc_cost(graph, set(), inp, out, 0))
# print(" -> ".join(path))
