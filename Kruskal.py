import networkx as nx
from matplotlib import pyplot as plt
from item import test_svaz

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):

        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)



        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            # print(e)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                # print([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)
        return result


# Driver code
g = Graph(9)

g.add_edge(0, 1, 2)
g.add_edge(0, 3, 2)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 3)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 6)
g.add_edge(4, 5, 4)
g.add_edge(3, 6, 7)
g.add_edge(5, 6, 8)
g.add_edge(7, 8, 4)

if test_svaz(g.graph):

    graph_g = nx.Graph()

    for i in range(0, 9):
        graph_g.add_node(i)

    for el in g.graph:
        graph_g.add_edge(el[0], el[1], weight=el[-1])

    options = {
        'node_color': 'pink',
        'node_size': 1000,
        # 'arrows': True,
        'with_labels': True,
        # 'arrowstyle': '-|>'
    }

    pos = nx.spring_layout(graph_g)
    nx.draw(graph_g, pos, **options)
    labels = nx.get_edge_attributes(graph_g, 'weight')
    nx.draw_networkx_edge_labels(graph_g, pos, edge_labels=labels)
    plt.show()

    # Function call

    T = g.KruskalMST()

    graph_t = nx.Graph()

    for i in range(0, 7):
        graph_t.add_node(i)

    for el in list(T):
        graph_t.add_edge(el[0], el[1], weight=el[-1])

    options = {
        'node_color': 'pink',
        'node_size': 1000,
        # 'arrows': True,
        'with_labels': True,
        # 'arrowstyle': '-|>'
    }

    pos = nx.spring_layout(graph_t)
    nx.draw(graph_t, pos, **options)
    labels = nx.get_edge_attributes(graph_t, 'weight')
    nx.draw_networkx_edge_labels(graph_t, pos, edge_labels=labels)
    plt.show()
