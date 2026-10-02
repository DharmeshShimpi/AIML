from collections import deque

def monkey_banana_bfs():

    graph = {
        "Monkey at Door": ["Monkey at Box"],
        "Monkey at Box": ["Box Under Banana"],
        "Box Under Banana": ["Monkey Climbs Box"],
        "Monkey Climbs Box": ["Monkey Gets Banana"],
        "Monkey Gets Banana": []
    }

    start = "Monkey at Door"
    goal = "Monkey Gets Banana"

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for next_state in graph[current]:
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)
    
    return None

solution = monkey_banana_bfs()
print("Solution path:")
for step in solution:
    print("->", step)
