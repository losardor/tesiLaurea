import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.cm as cm

x=[]
y=[]
for i in range(10):
	A, B=np.loadtxt("gameBeta"+str(float(i+1)/100)+".dat", delimiter='\t', unpack=True)
	x.append(A)
	y.append(B)
fig=plt.figure()
ax1=plt.subplot2grid((1,1),(0,0))
colors = cm.rainbow(np.linspace(0, 1, len(y)))
X=list(x[0])
i=0
for Y in list(y):
	plt.scatter(X, Y, marker='.', color=colors[i], label=str(float(i+1)/100))
	i+=1
plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')
plt.title('Number of Different Words in Time')
plt.legend()
ax1.grid(True)
plt.show()
last=[]
max=[]
betaas=[]
for i in range(10):
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