graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

goal = "F"

def dls(node, limit):
    print(f"Visiting {node}, depth left={limit}")
    if node == goal:
        return True
    if limit == 0:
        return False

    for child in graph[node]:
        if dls(child, limit - 1):
            return True
    return False

print("Found?", dls("A", 2))
