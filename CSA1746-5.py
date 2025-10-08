from collections import deque

def valid(state):
    m1, c1, boat, m2, c2 = state
    return (0 <= m1 <= 3 and 0 <= c1 <= 3 and 0 <= m2 <= 3 and 0 <= c2 <= 3 and 
           (m1 == 0 or m1 >= c1) and (m2 == 0 or m2 >= c2))

def successors(state):
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    m1, c1, boat, m2, c2 = state
    sign = -1 if boat else 1
    res = []
    for m,c in moves:
        ns = (m1 + sign*m, c1 + sign*c, 1 - boat, m2 - sign*m, c2 - sign*c)
        if valid(ns):
            res.append(ns)
    return res

def missionaries_cannibals():
    start = (3,3,1,0,0)
    goal = (0,0,0,3,3)
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            print(path)
            return
        for next_state in successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
                
missionaries_cannibals()
