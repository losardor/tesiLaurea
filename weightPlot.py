import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import cPickle as pk
import Agent
import seaborn as sns

sns.set(style="whitegrid")
sns.set_color_codes("pastel")
filename= "files/topolgy1080.pk"
with open(filename, 'rb') as input:
	G = pk.load(input)
for Beta in np.arange(0.003, 0.01, 0.001):
	for edge in G.edges():
		G[edge[0]][edge[1]]['weight'] = 2.7**(-Beta*abs(G.node[edge[0]]['height'] - G.node[edge[1]]['height']))
	edgeWeights=[d['weight'] for (u,v,d) in G.edges(data=True)]
	bins=np.arange(0.1,1,0.05)
	plt.figure(figsize=(12, 9))
	fig=plt.hist(edgeWeights, bins, histtype='bar', rwidth=0.8, label='Edge Weights')
	plt.xlabel('Edge Weights')
	plt.ylabel('Frequency')
	sns.despine(bottom=True)
	plt.title('Edge Weights\nThe frequency with witch a given weight is assigned given this DEM distribution')
	plt.savefig("weight_histogram_"+str(Beta), format='png')
