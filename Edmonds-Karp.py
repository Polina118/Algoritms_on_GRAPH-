import matplotlib.pyplot as plt
import networkx as nx
from functions_for_GRAPH import read_graf_from_file
from functions_for_GRAPH import inc_to_matrix


def max_flow(C, s, t):
    n = len(C)
    F = [[0] * n for i in range(n)]
    path = bfs(C, F, s, t)

    while path is not None:
        flow = min(C[u][v] - F[u][v] for u, v in path)
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
        path = bfs(C, F, s, t)
    print(F)

    graph_F = nx.DiGraph()

    for i in range(0, len(F)):
        for j in range(0, len(F)):
            if F[i][j] > 0:
                graph_F.add_edge(i, j, weight=F[i][j])

    options = {
        'node_color': 'pink',
        'node_size': 1000,
        'arrows': True,
        'with_labels': True,
        'arrowstyle': '-|>'
    }

    pos = nx.spring_layout(graph_F)
    nx.draw(graph_F, pos, **options)
    labels = nx.get_edge_attributes(graph_F, 'weight')
    nx.draw_networkx_edge_labels(graph_F, pos, edge_labels=labels)
    plt.show()

    return sum(F[s][i] for i in range(n))


#  BFS
def bfs(C, F, s, t):
    queue = [s]
    paths = {s: []}
    if s == t:
        return paths[s]
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if (C[u][v] - F[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                # print(paths)
                if v == t:
                    return paths[v]
                queue.append(v)
    return None

# capacity graph
###############################################
# print('введите количество вершин: ')
# v = int(input())
# M = []
# for i in range(v):
#     M.append([0 for _ in range(v)])
#
# print('введите количество ребер: ')
# e = int(input())
# for i in range(0, e):
#     print('введите ребро (начало, конец, вместимость): ')
#     a = int(input())
#     b = int(input())
#     capacity = int(input())
#     M[a][b] = capacity
#
# for i in range(len(M)):
#     print(M[i])
#
# print('введите исток: ')
# source = int(input())
# print('введите сток: ')
# sink = int(input())

###############################################

# M = [[0, 3, 0, 3, 0, 0, 0],  # 0
#      [0, 0, 4, 0, 0, 0, 0],  # 1
#      [3, 0, 0, 1, 2, 0, 0],  # 2
#      [0, 0, 0, 0, 2, 6, 0],  # 3
#      [0, 1, 0, 0, 0, 0, 1],  # 4
#      [0, 0, 0, 0, 0, 0, 9],  # 5
#      [0, 0, 0, 0, 0, 0, 0]]  # 6

M = read_graf_from_file()

M = inc_to_matrix(M, 0)

source = 0
sink = 6

graph = nx.DiGraph()

for i in range(0, len(M)):
    for j in range(0, len(M)):
        if M[i][j] != 0:
            graph.add_edge(i, j, weight=M[i][j])

options = {
    'node_color': 'pink',
    'node_size': 1000,
    'arrows': True,
    'with_labels': True,
    'arrowstyle': '-|>'
}

pos = nx.spring_layout(graph)
nx.draw(graph, pos, **options)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
plt.show()

max_flow_value = max_flow(M, source, sink)
print("Edmonds-Karp algorithm")
print("max_flow_value is:", max_flow_value)
