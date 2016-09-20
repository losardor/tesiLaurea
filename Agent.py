import random
import networkx as nx
from math import sqrt
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import gridItalia as gi
import numpy as np
from matplotlib import style
import cPickle as pk

style.use('fivethirtyeight')

DEBUG = 0
class Agent():
	nw = 0 # max id of different words
	words = [] # occurrences of single words in the population
	ndw = 0 # nr of different words
	
	def __init__(self, id=0):
		self.dict = []
		self.id = id
	
	def __str__(self):
		return "ID:" + str(self.id)+ " L:" + str(len(self.dict)) + " D:" + str(self.dict)
	
	def NewWord(self):
		w = Agent.nw
		Agent.words.append(0) # a new word occurs at last position: create slot
		if DEBUG: print "### NewWord: w:%d d:%s" % (w,str(Agent.words))
		Agent.nw += 1
		#self.ndw += 1
		#print w
		return w
	
	def AddWord(self, w):
		self.dict.append(w)
		if DEBUG: print "*** AddWord:", w, " |words|=", len(Agent.words)
		Agent.words[w] += 1
		if(Agent.words[w]==1):
			Agent.ndw += 1
		return w
	
	def EraseDict(self):
		for i in self.dict:
			Agent.words[i] -= 1
			if(Agent.words[i]==0):
				Agent.ndw -= 1
		self.dict = []

	def ChooseWord(self):
		if(self.dict):
			return random.choice(self.dict)
		else:
			return 999999

	def RemoveWord(self, w): #remove occurances of w
		while(w in self.dict):
			self.dict.remove(w)
			Agent.words[w] -= 1

class Folk():

	def __init__(self, N=10, topology=0, choice = 1, Beta = 0.1):
		self.N = N
		self.agent = []
		for i in range(N):
			self.agent.append(Agent(i))
		self.topology = Topology(self.agent, topology, choice, Beta)

	def __str__(self):
		ag = self.agent[0]
		s = "# Ndw:"+str(ag.ndw)+" Nw:"+str(ag.nw)+" Words:"+str(ag.words)+"\n"
		for i in range(len(self.agent)):
			s += "# "+str(self.agent[i]) + "\n"
		return s

	def EraseAll(self):
		ag = self.agent[0]
		for i in range(len(self.agent)):
			self.agent[i].EraseDict()
		ag.nw = ag.ndw = 0
		ag.words = []

	def Select(self):
		return self.topology.Select(self.agent)
		#return random.sample(self.agent, 2)

COMPLETE = 0
ERDOS    = 1; ERDOS_p = 0.5
GRID2D   = 2
GRID2DBAND = 3
GRID2DBAND_p = 0.01
BARABASI = 4; BARABASI_M = 4
GRIDONMAP = 5
SHOW = 0
WEIGHTED = 1

class Topology():

	def __init__(self, agent, id=COMPLETE, choice=1, Beta = 0.1):
		self.tipo = id
		if id != COMPLETE:
			N = len(agent)
		if id == ERDOS:
			self.G = nx.erdos_renyi_graph(N, ERDOS_p)
		elif id == BARABASI:
			self.G = nx.barabasi_albert_graph(N, BARABASI_M)
		elif id == GRID2D:
			L = sqrt(N)
			if (int(L) != L):
				raise Exception("Number of Agents is not a square number")
			self.G = nx.grid_2d_graph(int(L),int(L),True)
		elif id == GRID2DBAND:
			L = sqrt(N)
			if (int(L) != L):
				raise Exception("Number of Agents is not a square number")
			self.G = nx.grid_2d_graph(int(L),int(L),False)
			Edge_list = self.G.edges()
			middle = int(L/2)
			for a in Edge_list:
				if (a[0][0]==middle and a[1][0]==middle+1) or (a[1][0]==middle and a[0][0]==middle+1):
					self.G[a[0]][a[1]]['weight'] = GRID2DBAND_p
				else:
					self.G[a[0]][a[1]]['weight'] = 1.0
		elif id == GRIDONMAP:
			nodeColor=[]
			lisofrelevantsizes = [i*i*30 for i in range(1,30) if i*i < 10000]
			if N not in lisofrelevantsizes:
				print "the number of agents doesn't fit the grid, changing to closest possibility\n"
				N=min(lisofrelevantsizes, key=lambda x:abs(x-N))
				print "the closest number is: " + str(N) + "\n"
				#self.G = gi.topologyInit(N, choice, Beta)
			filename= "files/topolgy"+str(N)+".pk"
			with open(filename, 'rb') as input:
				self.G = pk.load(input)
			if choice == WEIGHTED:
				for edge in self.G.edges():
					self.G[edge[0]][edge[1]]['weight'] =  2.7**(-Beta*abs(self.G.node[edge[0]]['height'] - self.G.node[edge[1]]['height']))
					if DEBUG:
						print self.G[edge[0]][edge[1]]['weight']
					#print str(edge) + "\t" + str(G[edge[0]][edge[1]]['weight']) + str(G.node[edge[0]]['height']) + "\t" + str(G.node[edge[1]]['height'])
			else:
				for edge in self.G.edges():
					self.G[edge[0]][edge[1]]['weight']=1
					print "the number of edges in this simulation will be " + str(len(self.G.edges())) + " And the number of agents will be " + str(len(self.G.nodes()))

			for x in self.G.nodes():
				nodeColor.append(int(self.G.node[x]['height']))
			#target = open("node_height", "w")
			#for x in range(len(nodeColor)):
				#target.write(str(x)+"\t"+str(nodeColor[x])+"\n")
			if SHOW == 1:
				fig=plt.figure()
				elarge=[(u,v) for (u,v,d) in self.G.edges(data=True) if d['weight'] >=0.05]
				esmall=[(u,v) for (u,v,d) in self.G.edges(data=True) if d['weight'] <0.05]
				nx.draw_networkx_edges(self.G, pos={i:i for i in self.G.nodes()}, edgelist=elarge, width=2)
				nx.draw_networkx_edges(self.G, pos={i:i for i in self.G.nodes()}, edgelist=esmall, width=2, alpha=0.5,edge_color='b',style='dashed')
				nx.draw_networkx_nodes(self.G, pos={i:i for i in self.G.nodes()}, node_color=nodeColor, node_cmap=plt.cm.summer, node_size=20)
				plt.xlabel('X_grid identifier')
				plt.ylabel('Y_grid identifier')
				plt.title('The grid\nGenerated on the basis of given DEM')
				plt.show() # display
			self.len=len(self.G.nodes())
		i = 0
		for n in self.G:
			self.G.node[n]['agent'] = agent[i]
			i += 1
		if id == GRIDONMAP:
			edgeWeights=[d['weight'] for (u,v,d) in self.G.edges(data=True)]
			bins=np.arange(0,1.1,0.05)
	        plt.hist(edgeWeights, bins, histtype='bar', rwidth=0.8, label='Edge Weights')
	        plt.xlabel('Edge Weights')
	        plt.ylabel('Frequency')
	        plt.title('Edge Weights\nThe frequency with witch a given weight is assigned given this DEM distribution')
	        plt.show()
	    	if DEBUG==1:
	    		orderedWeights=sorted(edgeWeights)
	    		xs=range(len(edgeWeights))
	    		fig2=plt.figure()
	    		plt.scatter(xs, orderedWeights)
	    		plt.show()
	#agent_list = {x: agent[x] for x in range(N)}
	#nx.set_node_attributes(self.G, 'agent', agent_list)
	def Select(self, agent):
		if self.tipo == COMPLETE:
			return random.sample(agent, 2)
		elif(self.tipo == GRID2DBAND):
			s = random.choice(self.G.nodes())
			if(not self.G.neighbors(s)):
				return [None, None]
			w = self.G.degree(s,'weight')
			r = random.uniform(0.0,w)
			E = self.G.edges(s)
			sum = 0.0
			for a in E:
				sum += self.G[a[0]][a[1]]['weight']
				if sum >= r:
					break
			if s == a[0]:
				h = a[1]
			else:
				h = a[0]
			return [ self.G.node[s]['agent'], self.G.node[h]['agent']]
		else:
			s = random.choice(self.G.nodes())
			if(not self.G.neighbors(s)):
				return [None, None]
			mapping={key[:2]: key[2] for key in self.G.edges(s, data='weight')}
			link=nx.utils.random_sequence.weighted_choice(mapping)
			if link[0]==s:
				h = link[1]
			else:
				h = link[0]
			return [ self.G.node[s]['agent'], self.G.node[h]['agent'] ]