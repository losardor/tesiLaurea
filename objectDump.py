import cPickle as pk
import gridItalia as grd
import networkx as nx
from operator import itemgetter
import sys
from matplotlib import pyplot as plt
import matplotlib.colors as cm

DEBUG = 0
SHOW = 0
HEIGHT=6
WIDTH=5
DELTAS=75
ALTEZZAZ=500
ORDINE=1/ALTEZZAZ
WEIGHTED = 1

lisofrelevantsizes = [i*i*30 for i in range(5,30) if i*i < 10000]
FRACTION=0.2796296296296296
for N in lisofrelevantsizes:
	M=grd.mapInfo("files/Grid.xyz")
	coarsnes = int(((float(N)/FRACTION)/(WIDTH*HEIGHT))**(0.5))
	G = nx.grid_2d_graph(WIDTH*coarsnes, HEIGHT*coarsnes, True)
	listOfNodes = G.nodes()
	listOfPositions = M.getAll3dPos(G, coarsnes)
	listofGPS=[[element[0],element[1]] for element in listOfPositions]
	listOfHeights=[element[2] for element in listOfPositions]
	for i,x in enumerate(sorted(sorted(listOfNodes, key=itemgetter(0)), key=itemgetter(1), reverse=True)):
		G.node[x]['position']=listofGPS[i]
		G.node[x]['height']=listOfHeights[i]
	listOfNodes=[x for x in listOfNodes if float(G.node[x]['height']) == 0]
	G.remove_nodes_from(listOfNodes)
	print "the topology contains "+str(len(G.nodes()))+" nodes"
	filename = "files/topolgy"+str(N)+".pk"

	nodeColor=[]
	for x in G.nodes():
		nodeColor.append(int(G.node[x]['height']))
	AltezzaMassima=max(nodeColor)
	nodeColor=[float(color)/AltezzaMassima for color in nodeColor]

	fig=plt.figure(figsize=(16,12))
	fig.patch.set_facecolor('#F8F8ff')
	ax=plt.subplot(111)
	nodes=nx.draw_networkx_nodes(G, 
		pos={i:i for i in G.nodes()}, node_color=nodeColor, 
		node_cmap=cm.Colormap("terrain"),
		node_size=60)
	cbar=plt.colorbar(nodes, ticks=[0.5, 1])
	cbar.ax.set_yticklabels([str(AltezzaMassima/2),str(AltezzaMassima)])
	plt.xlabel('X_grid identifier')
	plt.ylabel('Y_grid identifier')
	plt.show()
	sys.stdout.flush()

	with open(filename, 'wb') as output:
		pk.dump(G, output, pk.HIGHEST_PROTOCOL)

