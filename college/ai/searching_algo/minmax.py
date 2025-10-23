import sys

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

values = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 1,
    "E": 2,
    "F": 3,
    "G": 4,
}

def min_max(
    values: dict[str, int],
    graph: dict,
    maximizingPlayer: bool,
    currNode: str,
) -> int:
    if len(graph[currNode]) == 0:
        return values[currNode]

    if maximizingPlayer:
        best = -sys.maxsize
        for n in graph[currNode]:
            val = min_max(values, graph, not maximizingPlayer, n)
            best = max(best, val)
    else:
        best = sys.maxsize
        for n in graph[currNode]:
            val = min_max(values, graph, not maximizingPlayer, n)
            best = min(best, val)

    return best

print(min_max(values, graph, True, "A"))
