graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()

def dfs(vertex):
    visited.add(vertex)

    print(vertex, end=" ")

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour)


start_vertex = 'A'
print("DFS Traversal")
dfs(start_vertex)