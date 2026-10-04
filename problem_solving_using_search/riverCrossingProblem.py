from collections import deque

def is_safe(state):
    # state is a string of 4 chars: F W G C (0=left, 1=right)
    F, W, G, C = state
    # Wolf and goat alone (farmer not with them)
    if W == G and F != W:
        return False
    # Goat and cabbage alone (farmer not with them)
    if G == C and F != G:
        return False
    return True

def river_crossing_bfs():
    start = "0000"
    goal  = "1111"

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    # possible items the farmer can take (or go alone)
    items = [0, 1, 2, 3]   # 0=farmer alone, 1=wolf, 2=goat, 3=cabbage

    while queue:
        current = queue.popleft()

        if current == goal:
            # rebuild path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        F = current[0]

        for i in items:
            # create new state by moving farmer and possibly one item
            new_state = list(current)
            # move farmer to the other side
            new_state[0] = '1' if F == '0' else '0'

            if i != 0:  # also move an item
                # item can move only if it is on the same side as farmer
                if current[i] == F:
                    new_state[i] = new_state[0]
                else:
                    continue   # cannot take that item

            new_state = ''.join(new_state)

            if new_state not in visited and is_safe(new_state):
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

    return None

# Run
solution = river_crossing_bfs()
print("Solution path (F W G C):")
for state in solution:
    print("→", state)