import cPickle as pk
import gridItalia as grd
import random
import networkx as nx
from operator import itemgetter
import matplotlib.pyplot as plt

def getAll3dPos(grid, M):
	listOfNodes = grid.nodes()
	positions=[G.node[n]['pos'] for n in grid]
	positions=sorted(sorted(positions, key=itemgetter(0)), key=itemgetter(1), reverse=True)
	print positions
	print "\n"
	plt.plot([item[0] for item in positions], [item[1] for item in positions])
	plt.show()

	calibratedpositions=[[item[0]*M.length+float(M.first[0]), float(M.first[1])-item[1]*M.height] for item in positions]
	print sorted(sorted(calibratedpositions, key=itemgetter(0)), key=itemgetter(1), reverse=True)
	print "\n"
	listofpointsx=[float(M.first[0])+inc*75 for inc in range(int(M.xrange))]
	listofpointsy=[float(M.first[1])-inc*75 for inc in range(int(M.yrange))]
	listPositions = [[min(listofpointsx, key=lambda x:abs(x-item[0]*M.length+float(M.first[0]))), min(listofpointsy, key=lambda x:abs(x-float(M.first[1])-item[1]*M.height))] for item in positions]
	listOfValues=sorted(sorted(listPositions, key=itemgetter(0)), key=itemgetter(1), reverse=True)
	print listOfValues
	ind=0
	values=listOfValues[ind]
	for currentline, line in enumerate(open(M.theFile, "rU")):
		if ((float( line.split()[1] )+37.5 >= float( values[1] )) and ((float( line.split()[1] )-37.5 < float( values[1] )))) and ((float( line.split()[0] )+37.5 >= float( values[0] )) and ((float( line.split()[0] )-37.5 < float( values[0] )))):
			listOfValues[ind].append(int(line.split()[2]))
			if (ind != len(listOfValues)-1):
				ind+=1
				values=listOfValues[ind]
			else:
				break
	return listOfValues

DEBUG = 0
SHOW = 0
HEIGHT=6
WIDTH=5
DELTAS=75
ALTEZZAZ=500
ORDINE=1/ALTEZZAZ
WEIGHTED = 1

lisofrelevantsizes = [i*i*30 for i in range(1,30) if i*i < 10000]
FRACTION=0.2796296296296296
for N in lisofrelevantsizes:
	print "I am processing size "+str(N)+"\n"
	M=grd.mapInfo("files/Grid.xyz")
	w = {i: random.expovariate(0.5) for i in range(N)}
	G = nx.geographical_threshold_graph(N, 500)
	listOfNodes = G.nodes()
	listOfPositions = getAll3dPos(G, M)
	listofGPS=[[element[0],element[1]] for element in listOfPositions]
	listOfHeights=[element[2] for element in listOfPositions]
	for i,x in enumerate(sorted(sorted(listOfNodes, key=itemgetter(0)), key=itemgetter(1), reverse=True)):
		G.node[x]['position']=listofGPS[i]
		G.node[x]['height']=listOfHeights[i]
	listOfNodes=[x for x in listOfNodes if float(G.node[x]['height']) == 0]
	G.remove_nodes_from(listOfNodes)
	filename = "files/topolgy_threshold"+str(N)+".pk"
	with open(filename, 'wb') as output:
		pk.dump(G, output, pk.HIGHEST_PROTOCOL)


