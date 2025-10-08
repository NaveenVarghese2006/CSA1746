from queue import PriorityQueue
def a_star(graph, start, goal, heuristic):
    pq = PriorityQueue()
    pq.put((0, start, [start]))
    visited = set()
    while not pq.empty():
        cost, node, path = pq.get()
        if node == goal:
            print("Path:", path, "Cost:", cost)
            return
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    ncost = cost + weight
                    pq.put((ncost + heuristic[neighbor], neighbor, path + [neighbor]))

graph = {'A':[('B',1),('C',4)], 'B':[('D',2),('E',5)], 'C':[('F',1)], 
         'D':[], 'E':[('F',1)], 'F':[]}
heuristic = {'A':4, 'B':2, 'C':2, 'D':0, 'E':0, 'F':0}
a_star(graph, 'A', 'F', heuristic)
