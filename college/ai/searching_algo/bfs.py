import queue

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}


def bfs(graph, start, goal):
    visited = set()
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        vertex = q.get()
        if vertex == goal:
            print(f"{vertex} > ", end="")
            return
        if vertex not in visited:
            print(f"{vertex} > ", end="")
            visited.add(vertex)

            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)


bfs(graph, "A", "C")
print()
