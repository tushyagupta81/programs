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
            print(f"{vertex}")
            return
        if vertex not in visited:
            print(f"{vertex} > ", end="")
            visited.add(vertex)

            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)


start = input("Starting Node: ").upper()
goal = input("Ending Node: ").upper()
bfs(graph, start, goal)
print()
