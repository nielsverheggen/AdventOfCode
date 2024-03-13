import networkx as nx
graph = nx.Graph([(l.split(':')[0], x) for l in open('input.txt').read().splitlines() for x in l.split(':')[1].strip().split(' ')])
graph.remove_edges_from(nx.minimum_edge_cut(graph))
print(len(list(nx.connected_components(graph))[0])*len(list(nx.connected_components(graph))[1]))
