from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left > 0 and m_left < c_left:
        return False
    
    if m_right > 0 and m_right < c_right:
        return False
    
    return True


def missionaries_cannibals():

    start = (3, 3, 'L')
    goal = (0, 0, 'R')

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:

        current = queue.popleft()

        if current == goal:
            break

        m_left, c_left, boat = current

        for m, c in moves:

            if boat == 'L':
                new_m = m_left - m
                new_c = c_left - c
                new_boat = 'R'
            
            else:
                new_m = m_left + m
                new_c = c_left + c
                new_boat = 'L'

            new_state = (new_m, new_c, new_boat)

            if (0 <= new_m <= 3 and 
                0 <= new_c <= 3 and
                is_valid(new_m, new_c) and
                new_state not in visited):

                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)

    if goal in visited:
        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        print("Solution:")
        for state in path:
            print(state)
    else:
        print("No solution found")
        
missionaries_cannibals()