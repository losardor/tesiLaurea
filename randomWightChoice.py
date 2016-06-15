#Random weightes choice try
import random as rnd
import networkx as nx
G = nx.Graph()
G.add_nodes_from(range(1,19))
nods=tuple(range(1,19))
edge=[]
for i in nods:
	for j in range(int(rnd.random()*19)):
		edge.append((i , int(rnd.random()*len(nods)) , rnd.random()))
G.add_weighted_edges_from(edge)
speaker=rnd.choice(G.nodes())
print speaker
mapping={key[:2]: key[2] for key in G.edges(speaker, data='weight')}
link=nx.utils.random_sequence.weighted_choice(mapping)
print link
if link[0]==speaker:
		hearer = link[1]
else:
	hearer = link[0]
print hearer