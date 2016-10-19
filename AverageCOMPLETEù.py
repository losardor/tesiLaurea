from Agent import *
from Game import Play
import matplotlib.pyplot as plt

sumNDW=[]
sumNW=[]
iter=10
for i in range(iter):
	runsNdw=[]
	runsNw=[]
	folk=Folk(1000, COMPLETE)
	runsNdw, runsNw =Play(folk, 100000)
	if sumNDW==[]:
		sumNDW=[Ndw for Ndw in runsNdw]
	else:
		sumNDW=[Ndw+sumNDW[i] for i, Ndw in enumerate(runsNdw)]

	if sumNW==[]:
		sumNW=[Nw for Nw in runsNw]
	else:
		sumNW=[Nw+sumNW[i] for i, Nw in enumerate(runsNw)]

averageNdw=[float(sumNdw)/iter for sumNdw in sumNDW]
averageNw=[float(sumNw)/iter for sumNw in sumNW]
target = open("averageComplete.dat", "w")
target.write("Time step\taverageNw\taverageNdw\n")
for i in range(len(averageNdw)):
	target.write(str(i)+"\t"+str(averageNw[i])+"\t"+str(averageNdw[i])+"\n")
target.close()
plt.plot(range(len(averageNdw)), averageNdw, label="NDW")
plt.plot(range(len(averageNw)), averageNw, color="red", label="NW")
plt.legend()
plt.show()