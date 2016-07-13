#Grid for italy
import networkx as nx
import getline as gl
import tailer as tl
import math as mt
import matplotlib.pyplot as plt

HEIGHT=6
WIDTH=5
DELTAS=75
ALTEZZAZ=500
ORDINE=1/ALTEZZAZ

class mapInfo():
 	"""This object takes a text formatted Dem grid mapInfo"""
 	def __init__(self, theFile):
 		self.theFile = theFile
 		self.first = tl.head(open(theFile),1)[0].split()
 		print "the top left corner has position: " + self.first[0] + "\t"+ self.first[1]
 		self.last = tl.tail(open(theFile),1)[0].split()
 		print "the bottom right corner has position: " + self.last[0] + "\t" + self.last[1]
		self.yrange=abs((float(self.last[1])-float(self.first[1]))/DELTAS)
		print "the  y-range of our map in boxes: " + str(self.yrange)
		self.xrange=abs((float(self.last[0])-float(self.first[0]))/DELTAS)
		print "the  x-range of our map in boxes: " + str(self.xrange)

	def positionFromIndex(self, index, coarsnes):
	
		self.positionx = (int(index[0])+1)*self.xrange*DELTAS/(WIDTH*coarsnes)
		self.positiony = (int(index[1])+1)*self.yrange*DELTAS/(HEIGHT*coarsnes)
		self.position = [self.positionx, self.positiony]
		return self.position

	def getHeight(self, position):
		self.place=position
		line=int((float(self.place[0])/DELTAS)*float(self.place[1])/DELTAS + float(place[0]/DELTAS))-1
		self.height=gl.getline(self.theFile, line).split()[2]
		return self.height

	def getallHeights(self, grid, coarsnes):
		listof_nodes=grid.nodes()
		listof_nodes=[self.positionFromIndex(item, coarsnes) for item in listof_nodes]
		lines=[int((float(place[0])/DELTAS)*float(place[1])/DELTAS + float(place[0]/DELTAS))-1 for place in listof_nodes]
		linesdict = {lines[i]:i for i in range(len(lines))}
		out = [0 for i in range(len(lines))]
		values = linesdict.keys()
		values.sort()
		ind=0
		for currentline, line in enumerate(open(self.theFile, "rU")):
			if currentline == values[ind]:
				out[linesdict[currentline]] = int(line.split()[2])
				if(ind!=len(values)-1): 
					ind+=1
				else: break
		return out

	
def topologyInit(N):
	FRACTION=0.2796296296296296
	M=mapInfo("files/Grid.xyz")
	coarsnes = int(((float(N)/FRACTION)/(WIDTH*HEIGHT))**(0.5))
	print "Coarsness is : " + str(coarsnes)
	G = nx.grid_2d_graph(HEIGHT*coarsnes, WIDTH*coarsnes, True)
	listOfNodes = G.nodes()
	totalNum = len(listOfNodes)
	listOfHeights = M.getallHeights(G, coarsnes)
	for x in listOfNodes:
		G.node[x]['position']=M.positionFromIndex(x, coarsnes)
	nodeColor=[]
	for x in range(len(listOfNodes)):
		G.node[listOfNodes[x]]['height']=listOfHeights[x]
	listOfNodes=[x for x in listOfNodes if float(G.node[x]['height']) == 0]
	print "The actual number of agents in this simulation will be " + str(len(G.nodes()))
	G.remove_nodes_from(listOfNodes)
	for edge in G.edges():
		G[edge[0]][edge[1]]['weight']=((1.0+abs(G.node[edge[0]]['height'] - G.node[edge[1]]['height']))**(-1))/0.325
		print G[edge[0]][edge[1]]['weight']
		#print str(edge) + "\t" + str(G[edge[0]][edge[1]]['weight']) + str(G.node[edge[0]]['height']) + "\t" + str(G.node[edge[1]]['height'])
	print len(G.edges())
	for x in G.nodes():
		nodeColor.append(int(G.node[x]['height']))
	elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >=0.05]
	esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <0.05]
	nx.draw_networkx_edges(G, pos={i:i for i in G.nodes()}, edgelist=elarge, width=2)
	nx.draw_networkx_edges(G, pos={i:i for i in G.nodes()}, edgelist=esmall, width=2, alpha=0.5,edge_color='b',style='dashed')
	nx.draw_networkx_nodes(G, pos={i:i for i in G.nodes()}, node_color=nodeColor, node_cmap=plt.cm.gist_earth, node_size=20)
	plt.savefig("the_grid.png") # save as png
	plt.show() # display
	return G

def main():
	fraction=[]
	M = mapInfo("files/Grid.xyz")
	for coarsnes in range(6,7):
		print "#- Map for coarsnes: " + str(coarsnes)
		G = nx.grid_2d_graph(HEIGHT*coarsnes, WIDTH*coarsnes, True)
		listOfNodes = G.nodes()
		totalNum = len(listOfNodes)
		listOfHeights=M.getallHeights(G, coarsnes)
		for x in listOfNodes:
			G.node[x]['position']=M.positionFromIndex(x, coarsnes)
		for x in range(len(listOfNodes)):
			G.node[listOfNodes[x]]['height']=listOfHeights[x]
		for x in listOfNodes:
			print "--Node ({0}, {1}):\t {2}\t{3}\t{4}".format(x[0],
			 x[1], G.node[x]['position'][0], G.node[x]['position'][1], 
			 G.node[x]['height']) 
		listOfNodes=[x for x in listOfNodes if int(G.node[x]['height']) == 0]
		print listOfNodes
		G.remove_nodes_from(listOfNodes)
		len(G.nodes())
		fraction.append(float(len(G.nodes()))/totalNum)
	print "For each coarsnes the respective fraction of existing nodes is:"
	print fraction

def test():
	M=mapInfo("files/Grid.xyz")
	coarsness=1
	G = nx.grid_2d_graph(HEIGHT*coarsness, WIDTH*coarsness, True)
	print M.getallHeights(G, coarsness)


if __name__ == "__main__": main()