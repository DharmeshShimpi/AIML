# Depth Limited Search

def dls(graph, node, goal, limit):

    # Goal is found
    if node == goal:
        return True

    # Depth limit reached
    if limit == 0:
        return False

    # Search each child
    for child in graph.get(node, []):
        if dls(graph, child, goal, limit - 1):
            return True

    return False


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Starting node, goal and depth limit
start = 'A'
goal = 'G'
limit = 2

# Perform DLS
if dls(graph, start, goal, limit):
    print("Goal found")
else:
    print("Goal not found within depth limit")