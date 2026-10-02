from collections import deque

def water_jug_bfs():
    start = (0, 0)
    goal_amount = 2

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        x, y = current

        if x == goal_amount or y == goal_amount:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        possible_states = [
            (4, y),
            (x, 3),
            (0, y),
            (x, 0),
            (max(0, x - (3 - y)), min(3, x + y)),
            (min(4, x + y), max(0, y - (4 - x)))
        ]

        for next_state in possible_states:
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = current
                queue.append(next_state)
        
    return none

solution = water_jug_bfs()
print("Solution path (4-litre, 3-litre): ")
for state in solution:
    print("->", state)