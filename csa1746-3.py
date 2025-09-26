def water_jug_problem(jug1, jug2, target):
    visited = set()
    queue = [(0, 0)]
    while queue:
        a, b = queue.pop(0)
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(f"Jug1: {a}, Jug2: {b}")
        if a == target or b == target:
            print("Target reached!")
            return
        moves = [(jug1, b), (a, jug2), (0, b), (a, 0),
                 (max(a + b - jug2, 0), min(a + b, jug2)),
                 (min(a + b, jug1), max(a + b - jug1, 0))]
        queue.extend(moves)
    print("No solution.")

jug1 = int(input("Enter capacity of jug 1: "))
jug2 = int(input("Enter capacity of jug 2: "))
target = int(input("Enter target volume: "))
water_jug_problem(jug1, jug2, target)
