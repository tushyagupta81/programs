import heapq

graph = {
    "A": [("B", 3), ("C", 5)],
    "B": [("D", 4), ("E", 10)],
    "C": [("F", 20), ("G", 9)],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}


def best_first(graph: dict[str, list[tuple[str, int]]], start: str, goal: str):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        _, node, path = heapq.heappop(pq)
        print(f"{node} ", end="")
        if node == goal:
            return path

        visited.add(node)

        for n, cost in graph[node]:
            if n not in visited:
                heapq.heappush(pq, (cost, n, path + [n]))


path = best_first(graph, "A", "E")
print()
print(f"Path = {path}")
