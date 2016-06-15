import random
import networkx as nx
from math import sqrt
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import griditalia as gi


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

   def RemoveWord(self, w): #removes ALL the occurrences of w
      while(w in self.dict):
	 self.dict.remove(w)
	 Agent.words[w] -= 1

      
class Folk():
	
	def __init__(self, N=10, topology=0):
    	self.N = N
      	self.agent = []
      	for i in range(N):
      		self.agent.append(Agent(i))
      	self.topology = Topology(self.agent, topology)
        
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
GRIDONMAP=5

class Topology():
   	def __init__(self, agent, id=COMPLETE):
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
			selg.G = gi.topologyInit(N)

	       
	    
	 	i = 0
	 	for n in self.G:
	    	self.G.node[n]['agent'] = agent[i]
	    	i += 1
      	if id!= COMPLETE: 
        	pos=nx.spring_layout(self.G)
        	nx.draw(self.G)
	    
	 #agent_list = {x: agent[x] for x in range(N)}
	 #nx.set_node_attributes(self.G, 'agent', agent_list)
      
   	def Select(self, agent):
      	if self.tipo == COMPLETE:
	 		return random.sample(agent, 2)
      	elif(self.tipo == GRID2DBAND):
	 		s = random.choice(self.G.nodes())
	 	if(not self.G.neighbors(s)): # if no neighs
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
	 		return [ self.G.node[s]['agent'], self.G.node[h]['agent'] ]
      	else:
	 		#s = random.choice(range(len(agent)))
	 		#h = random.choice(range(len(agent)))
	 		s = random.choice(self.G.nodes())
	 			if(not self.G.neighbors(s)): # if no neighs
	   				 return [None, None]
	 
	 h = random.choice(self.G.neighbors(s))
	 return [ self.G.node[s]['agent'], self.G.node[h]['agent'] ]
	 #return [agent[s],agent[h]]
      
      