import networkx as nx
from matplotlib import pyplot as plt
from matplotlib import cm
import cPickle as pk
import numpy as np


betas=[float(x)/100000 for x in range(50,1000, 25)]
for x in betas:
	print x
	with open("Postprocessing/Data/final_grid_gameBeta"+str(x)+"Prob1.dat",'rb') as file:
		G=pk.load(file)
		nodeColor=[]
		for j in G.nodes():
			nodeColor.append(sum([float(G[j][i]['weight'])/sum([weight[2] for weight in G.edges(i, data='weight')]) for i in G[j]]))

		for n in range(len(nodeColor)):
			nodeColor[n]=float(nodeColor[n]/max(nodeColor))

		fig2=plt.figure(figsize=(16,12))
		nodes=nx.draw_networkx_nodes(G, 
			pos={i:i for i in G.nodes()}, node_color=nodeColor, 
			node_cmap=cm.coolwarm, node_size=60)
		cbar=fig2.colorbar(nodes, ticks=[0, 1])
		plt.xlabel('X_grid identifier')
		plt.ylabel('Y_grid identifier')
		plt.show()