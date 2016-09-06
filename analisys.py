import numpy as np
from matplotlib import pyplot as plt
x1, y1 = np.loadtxt('gameBeta_un.dat', delimiter='\t', unpack=True)
x2, y2 = np.loadtxt('gameBeta.dat', delimiter='\t', unpack=True)
fig=plt.figure()
ax1=plt.subplot2grid((1,1),(0,0))
plt.scatter(x1, y1, color='r', marker='.', label='unweighted')
plt.scatter(x2, y2, color='b', marker='.', label='weighted')
plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')
plt.title('Number of Different Words in Time')
plt.legend()
ax1.grid(True)
plt.show()