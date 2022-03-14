import networkx as nx
import networkx.algorithms.isomorphism as iso
from networkx.algorithms import isomorphism
G1 = nx.path_graph(4)
G2 = nx.path_graph(4)
GM = isomorphism.GraphMatcher(G1, G2)

print(GM.is_isomorphic())

G3 = nx.DiGraph()
G4 = nx.DiGraph()
nx.add_path(G3, [1, 2, 3, 4], weight=1)
nx.add_path(G4, [10, 20, 30, 40], weight=2)
em = iso.numerical_edge_match("weight", 1)
print(nx.is_isomorphic(G3, G4))  # no weights considered


g8=nx.Graph()
g8.add_nodes_from(['1','2','3','4'])
g8.add_edges_from([('1','2'),('1','3'),('2','4'),('3','4')])
print(nx.draw(g8))
nx.is_isomorphic(g8, G4)













