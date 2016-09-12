import numpy as np
from matplotlib import pyplot as plt
x1, y1 = np.loadtxt('gameBeta0.1.dat', delimiter='\t', unpack=True)
x2, y2 = np.loadtxt('gameBeta0.01.dat', delimiter='\t', unpack=True)
x3, y3 = np.loadtxt('gameBeta0.02.dat', delimiter='\t', unpack=True)
x4, y4 = np.loadtxt('gameBeta0.03.dat', delimiter='\t', unpack=True)
x5, y5 = np.loadtxt('gameBeta0.04.dat', delimiter='\t', unpack=True)
x6, y6 = np.loadtxt('gameBeta0.05.dat', delimiter='\t', unpack=True)
x7, y7 = np.loadtxt('gameBeta0.06.dat', delimiter='\t', unpack=True)
x8, y8 = np.loadtxt('gameBeta0.07.dat', delimiter='\t', unpack=True)
x9, y9 = np.loadtxt('gameBeta0.08.dat', delimiter='\t', unpack=True)
x10, y10 = np.loadtxt('gameBeta0.09.dat', delimiter='\t', unpack=True)
fig=plt.figure()
ax1=plt.subplot2grid((1,1),(0,0))
plt.scatter(x1, y1, color='#d14b47', marker='.', label='weight = 0.1')
plt.scatter(x2, y2, color='#ffc995', marker='.', label='weight = 0.01')
plt.scatter(x3, y3, color='#fd85a3', marker='.', label='weight = 0.02')
plt.scatter(x4, y4, color='#c28fce', marker='.', label='weight = 0.03')
plt.scatter(x5, y5, color='#a296a5', marker='.', label='weight = 0.04')
plt.scatter(x6, y6, color='#a015f1', marker='.', label='weight = 0.05')
plt.scatter(x7, y7, color='#9cd105', marker='.', label='weight = 0.06')
plt.scatter(x8, y8, color='#cd426d', marker='.', label='weight = 0.07')
plt.scatter(x9, y9, color='#a4c75c', marker='.', label='weight = 0.08')
plt.scatter(x10, y10, color='#0796bc', marker='.', label='weight = 0.09')
plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')
plt.title('Number of Different Words in Time')
plt.legend()
ax1.grid(True)
plt.show()