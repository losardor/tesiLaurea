import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
x=[]
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)
y=[]
for i in range(2,19):
	A, B=np.loadtxt("gameBeta"+str(0.0005+0.0005*i)+"Prob1.dat", delimiter='\t', unpack=True)
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
#plt.yticks(range(beginning, end, icrement), [str(x)+"%" for x in range(beginning, end, increment)], fontsize=14)
plt.xticks(fontsize=14)
#
# Provide tick lines across the plot to help your viewers trace along    
# the axis ticks. Make sure that the lines are light and small so they    
# don't obscure the primary data lines.    
#for y in range(10, 91, 10):    
#    plt.plot(range(1968, 2012), [y] * len(range(1968, 2012)), "--", lw=0.5, color="black", alpha=0.3)    
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")


colors = cm.rainbow(np.linspace(0, 1, len(y)))
X=list(x[0])
for rank,Y in enumerate(list(y)):
	plt.scatter(X, Y, marker='.', color=tableau20[rank], label="beta= "+str(0.005+0.00025*(rank+3)))
plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')
plt.title('Number of Different Words in Time')

plt.legend()
plt.show()
'''
last=[]
max=[]
betaas=[]
for i in range(19):
	last.append(y[i][-1])
	max.append(y[i].max())
	betaas.append(float(i+1)/100)
plt.scatter(betaas,last, marker='*', color='r', label='the last ndw')
#plt.scatter(betaas, max, marker='.', color='b', label='The max ndw')
plt.xlabel('Beta')
plt.ylabel('Number of different words')
plt.title('The maximum and last value of the number of different words as a function of the weight beta')
plt.legend()
plt.show()
'''