import math

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
    "D": 4,
    "E": 3,
    "F": 2,
    "G": 1,
}


def alpha_beta(
    values: dict[str, int],
    graph: dict,
    maximizingPlayer: bool,
    currNode: str,
    alpha: float,
    beta: float,
) -> float:
    if len(graph[currNode]) == 0:
        return values[currNode]

    if maximizingPlayer:
        best = -math.inf
        for n in graph[currNode]:
            val = alpha_beta(values, graph, not maximizingPlayer, n, alpha, beta)
            alpha = max(alpha, val)
            best = max(best, val)
            if alpha >= beta:
                print(f"Pruning at {currNode}")
                break
    else:
        best = math.inf
        for n in graph[currNode]:
            val = alpha_beta(values, graph, not maximizingPlayer, n, alpha, beta)
            beta = min(beta, val)
            best = min(best, val)
            if alpha >= beta:
                print(f"Pruning at {currNode}")
                break

    return best


print(alpha_beta(values, graph, True, "A", -math.inf, math.inf))
