import itertools

def tsp(graph, start):
    nodes = list(graph.keys())
    min_cost = float('inf')
    min_path = []
    for perm in itertools.permutations([n for n in nodes if n != start]):
        cost, cur = 0, start
        for n in perm:
            cost += graph[cur][n]
            cur = n
        cost += graph[cur][start]
        if cost < min_cost:
            min_cost = cost
            min_path = [start] + list(perm) + [start]
    print("Path:", min_path)
    print("Cost:", min_cost)

graph = {'A':{'B':10,'C':15,'D':20}, 'B':{'A':10,'C':35,'D':25}, 
         'C':{'A':15,'B':35,'D':30}, 'D':{'A':20,'B':25,'C':30}}
tsp(graph, 'A')
