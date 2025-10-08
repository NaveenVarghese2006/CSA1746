def vacuum_cleaner():
    # 2 rooms labelled A and B, both can be 'clean' or 'dirty'
    # Simulation of agent actions
    states = [('A','dirty','dirty'), ('A','clean','dirty'), ('A','dirty','clean'), ('A','clean','clean')]
    for location, a, b in states:
        print(f"Location: {location}, Room A: {a}, Room B: {b}")
        if location == 'A':
            if a == 'dirty':
                a = 'clean'
            location = 'B'
        if location == 'B':
            if b == 'dirty':
                b = 'clean'
        print(f"Result: Room A: {a}, Room B: {b}")
vacuum_cleaner()
