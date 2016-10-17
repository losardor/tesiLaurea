from Agent import *
from Game import Play
import matplotlib.pyplot as plt

folk=Folk(10000, COMPLETE)
runsNw=[]
runsNdw=[]
sumNDW=[]
sumNW=[]

for i in range(1000):
	runsNdw, runNw =Play(folk, 100000)
	if sumNDW==[]:
		sumNDW=[Ndw for Ndw in runsNdw]
	else:
		sumNDW=[Ndw+sumNDW[i] for i, Ndw in enumerate(runsNdw)]

	if sumNW==[]:
		sumNW=[Nw for Nw in runsNw]
	else:
		sumNW=[Nw+sumNW[i] for i, Nw in enumerate(runsNw)]

averageNdw=[sumNdw/1000 for sumNdw in sumNDW]
averageNw=[sumNw/1000 for sumNw in sumNW]
plt.plot(range(len(averageNdw)), averageNdw, label="NDW")
plt.plot(range(len(averageNw)), averageNw, color="red", label="NW")
plt.legend()
plt.show()