import numpy as np
from matplotlib import pyplot as plt

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
z=[]
A, B, C=np.loadtxt("gameBeta0.1Prob1.dat", delimiter='\t', unpack=True)
x.append(A)
y.append(B)
z.append(C)
A, B=np.loadtxt("grid2d.dat", delimiter='\t', unpack=True)
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
plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

X=list(x[0])
for rank,Y in enumerate(list(y)):
	if rank == 0:
		plt.scatter(X, Y, marker='.', color=tableau20[rank], label="complete")
	else:
		plt.scatter(X, Y, marker='.', color=tableau20[rank], label="grid2d")
plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')
plt.title('Number of Different Words in Time')

plt.legend()
plt.show()