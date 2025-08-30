# Breaadth-First Tree Seatch (BFS) Algortithm

# Understand this and be able to draw it
# S0 or N 
# S = State ( config of your enviroemnt)
# N = node in the graph or tree( node has state, action to get there, refrence to partent node)
# Build tuple (state, action(to reach that state), parent node) Or just use a class (do the class makes it easier and mroe readable)


# Using graph
# Use an explored set data structure

# Build
# Action method
# transition method

# Use graph for assignment

# make into class(state, action, parent node)




from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["V"],
    "C": ["D"],
    "D": ["E"],
    "E": [],
    "V": ["E"]
}


start = "A"
goal = "E"

# init.                #init the frontier as an empty FIFO que
q = deque([start])
visisted = {start}
parent = {start: None}



while q:

    node = q.popleft()
    print("proccessing", node)

    if node == goal:
        break

    for child in graph[node]:
        if child not in visisted:   
            visisted.add(child)
            parent[child] = node
            q.append(child)


print("visted", visisted)
print("parent", parent)


path = []
n = goal 
while n is not None:

    path.append(n)
    n = parent[n]
path.reverse()

print("path", path)
    

        
