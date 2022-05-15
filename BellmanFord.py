import networkx as nx
from matplotlib import pyplot as plt
from sys import maxsize

def BellmanFord(graph, V, E, src):
	dis = [maxsize] * V # l
	dis[src] = 0

	for i in range(V - 1):
		for j in range(E):
			if dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]:
				dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]

	for i in range(E):
		x = graph[i][0]
		y = graph[i][1]
		weight = graph[i][2]
		if dis[x] != maxsize and dis[x] + weight < dis[y]:
			print("Graph contains negative weight cycle")

	print("Vertex Distance")
	for i in range(V):
		print("%d\t\t%d" % (i, dis[i]))


V = 5  # vertices
E = 8  # edges

graph = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, -2], [1, 4, 2], [3, 2, -5], [3, 1, 1], [4, 3, -3]]
BellmanFord(graph, V, E, 0)

g = nx.Graph()
for i in range(1, V):
	g.add_node(i)

for el in list(graph):
	g.add_edge(el[0], el[1], weight=el[-1])

options = {
        'node_color': 'pink',
        'node_size': 1000,
        'arrows': True,
        'with_labels': True,
        'arrowstyle': '-|>'
}

pos = nx.spring_layout(g)
nx.draw(g, pos, **options)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

plt.show()
