def is_valid(node, color, colors, graph):
    for neighbor in graph[node]:
        if colors.get(neighbor) == color:
            return False
    return True

def color_map(graph, nodes, colors_list, colors={}, idx=0):
    if idx == len(nodes):
        print(colors)
        return True
    node = nodes[idx]
    for color in colors_list:
        if is_valid(node, color, colors, graph):
            colors[node] = color
            if color_map(graph, nodes, colors_list, colors, idx+1):
                return True
            colors[node] = None
    return False

graph = {'A':['B','C'], 'B':['A','C','D'], 'C':['A','B','D'], 'D':['B','C']}
nodes = list(graph.keys())
colors_list = ['Red','Green','Blue']
color_map(graph, nodes, colors_list)
