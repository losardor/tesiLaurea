#Grid for italy
import networkx as nx
import getline as gl

HEIGHT=5
WIDTH=4
DELTAS=75

def positionFromIndex(index, coarsnes)
	#rivedi come si fa con dizionario
	positionx=index%(WIDTH*coarsnes)*DELTAS
	positiony=index/(WIDTH*coarsnes)*DELTAS
	position=[positionx, positiony]
	return position

class mapInfo():
 	"""Thi fos object takes a text formatted Dem grid mapInfo"""
 	def __init__(self, theFile):
 		self.theFile = theFile
 		self.first = gl.getline(self.theFile, 1).split("\t")
 		self.length=len(enumerate(open(self.theFile, "rU")))
 		self.last = gl.getline(theFile,self.length).split("\t")
		self.xrange=(self.last[1]-self.first[1])/DELTAS #da controllare che gira con stringhe incece che numeri
		self.yrange=(self.last[0]-self.first[0])/DELTAS

	def getHeight(self, position)
		self.position=position
		self.height=gl.getline(self.theFile, position[1]/DELTAS+position[2]/DELTAS).split("t")[2]
		return self.height



	


fraction=[]
for coarsnes in range(1,7)
	G=nx.grid_2d_graph(HEIGHT*coarsnes, WIDTH*coarsnes, True)
	listOfNodes = G.nodes()
	totalNum=len(listOfNodes)
	listOfPos = [positionFromIndex(x,coarsnes) for x in listOfNodes]
	G.node[G.nodes]['position']=listOfPos
	M=mapInfo("files/Grid.xyz")
	listOfHeight = [M.getHeight(position) for position in listOfPos]
	G.node[G.nodes]['height']=listOfHeight
	listOfNodes=[x for x in G.nodes() if(! G.node[x]['height'])]
	G.remove_nodes_from(listOfNodes)
	fraction.append(len(G.nodes())/totalNum)

print fraction

 