import math
import networkx as nx
import matplotlib.pyplot as plt
def inc_to_list(graf):
    n = max(graf, key=lambda x: x[0])
    n2 = max(graf, key=lambda x: x[1])
    n = n[0] if n[0] > n2[1] else n2[1]
    new_graf = [[] for j in range(n + 1)]
    for i in graf:
        new_graf[i[0]].append(i[1])
    return new_graf

def inc_to_matrix(graf, seter=math.inf):
    n = max(graf, key=lambda x: x[0])
    n2 = max(graf, key=lambda x: x[1])
    n = n[0] if n[0] > n2[1] else n2[1]
    new_graf = [[seter for i in range(n + 1)] for j in range(n + 1)]
    for i in graf:
        new_graf[i[0]][i[1]] = i[2]
    return new_graf

def matrix_to_inc(graf, weight=False):
    new_graf = []
    for i in range(0, len(graf)):
        for j in range(0, len(graf[i])):
            if graf[i][j] != math.inf:
                if weight:
                    new_graf.append([i, j, graf[i][j]])
                else:
                    new_graf.append([i, j])
    return new_graf

def matrix_to_list(graf):
    new_graf = [[] for i in range(len(graf))]
    for i in range(0, len(graf)):
        for j in range(0, len(graf[i])):
            if graf[i][j] != math.inf:
                new_graf[i].append(j)
    return new_graf

def draw(graf, orgr=False, title="", weight=False):
    G = nx.DiGraph()
    plt.gcf().canvas.set_window_title(title)
    if weight:
        G.add_weighted_edges_from(graf, arrows=orgr)
        pos = nx.spring_layout(G)
        nx.draw_networkx(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    else:
        G.add_edges_from(graf)
        nx.draw_networkx(G, arrows=orgr, node_color='r')
    plt.show()

def test_svaz(graf):
    graf = inc_to_list(graf)
    visited = set()
    queue = set()
    visited.add(0)
    queue.add(0)
    while queue:
        vertex = queue.pop()
        for neighbour in graf[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.add(neighbour)
    if len(visited) < len(graf):
        print("Ошибка граф не связный")
        return 0
    else:
        return 1

def read_graf_from_file():
    graf = []
    with open('graf.txt') as f:
        temp = f.readlines()
        for i in temp:
            graf.append(list(map(int, i.split(" "))))
    return graf

def inc_to_matrix(graf, seter=math.inf):
    n = max(graf, key=lambda x: x[0])
    n2 = max(graf, key=lambda x: x[1])
    n = n[0] if n[0] > n2[1] else n2[1]
    new_graf = [[seter for i in range(n + 1)] for j in range(n + 1)]
    for i in graf:
        new_graf[i[0]][i[1]] = i[2]
    return new_graf