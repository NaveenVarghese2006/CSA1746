def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    print(node, end=' ')
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {'A':['B','C'], 'B':['D','E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
dfs(graph, 'A')  # Output: A B D E F C
