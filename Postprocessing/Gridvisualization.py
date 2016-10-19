import networkx as nx
from matplotlib import pyplot as plt
import cPickle as pk
import numpy as np

betas=[float(x)/100000 for x in range(50,1000, 25)]
for x in betas:
	with open("Data/final_grid_gameBeta"+str(x)+"Prob1.dat",'rb') as file:
		G=pk.load(file)
		edgeWeights=[d['weight'] for (u,v,d) in G.edges(data=True)]
		bins=np.arange(0.1,1,0.05)
		plt.hist(edgeWeights, bins, histtype='bar', rwidth=0.8, 
			label='Edge Weights')
		plt.xlabel('Edge Weights')
		plt.ylabel('Frequency')
		plt.title('Edge Weights\nThe frequency with witch a given weight is assigned given this DEM distribution')
		plt.show()

nodeColor=[]
for x in G.nodes():
	if G.node[x]['agent'].dict != []:
		nodeColor.append(int(G.node[x]['agent'].dict[0]))
	else:
		nodeColor.append(0)


for x in range(len(nodeColor)):
	nodeColor[x]=float(nodeColor[x]/max(nodeColor))
