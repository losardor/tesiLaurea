import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

betas=[float(x)/1000 for x in range(3, 51)]

x=[]
y=[]
for i in betas:
	time, A, B=np.loadtxt("Data/gameBeta"+str(i)+"Prob1.dat", 
		delimiter='\t', unpack=True)
	x.append(A)
	y.append(B)

fig=plt.figure(figsize=(16,12))
ax=plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.xticks(fontsize=14)   
plt.tick_params(axis="both", which="both", bottom="off", top="off", 
	labelbottom="on", left="off", right="off", labelleft="on")

colors = cm.rainbow(np.linspace(0, 1, len(x)))

for rank,X in enumerate(list(x)):
	if rank in range(0,len(x)):
		plt.plot(time, X, color=colors[rank], 
			label=str(betas[rank]), linewidth=1)

plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')

plt.legend()
plt.show()

last=[]
max=[]
betaas=[]
for i in range(len(x)):
	#last.append(x[i][-1])
	max.append(x[i].max())
	betaas.append(float(i+1)/100)

plt.scatter(betaas,max, marker='*', color='r', label='the maximal NDW')
plt.xlabel('Beta')
plt.ylabel('Number of different words')
plt.legend()
plt.show()