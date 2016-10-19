#Script for the test of palettes

import cPickle as pk
import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

with open("final_grid_gameBeta0.1Prob1.dat", 'rb') as file:
	G=pk.load(file)
uninteractingnodes=[x for x in G.nodes() if G.node[x]['agent'].dict==[]]
G.remove_nodes_from(uninteractingnodes)
nodeColor=[G.node[x]['agent'].dict[0] for x in G.nodes()]
for x in range(len(nodeColor)):
	nodeColor[x]=float(nodeColor[x])/(max(nodeColor))
difcolor=[]
for x in nodeColor:
	if x not in difcolor:
		difcolor.append(x)

numberofcolors=len(difcolor)
print numberofcolors

fig1=sns.palplot(sns.diverging_palette(240,10, n=numberofcolors))
plt.show()

palette=sns.diverging_palette(240, 10, as_cmap=True)
sns.palplot(palette(1.0))
plt.show()

fig2=nx.draw(G, 
	pos={i:i for i in G.nodes()}, 
	node_color=nodeColor, 
	node_cmap=sns.diverging_palette(240, 10, as_cmap=True), 
	node_size=20)
plt.show()