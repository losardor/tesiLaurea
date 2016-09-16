import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
current_palette = sns.color_palette()
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
plt.plot(x2, y2, marker='.', label='weight = 0.01')
plt.plot(x3, y3, marker='.', label='weight = 0.02')
plt.plot(x4, y4, marker='.', label='weight = 0.03')
plt.plot(x5, y5, marker='.', label='weight = 0.04')
plt.plot(x6, y6, marker='.', label='weight = 0.05')
plt.plot(x7, y7, marker='.', label='weight = 0.06')
plt.plot(x8, y8, marker='.', label='weight = 0.07')
plt.plot(x9, y9, marker='.', label='weight = 0.08')
plt.plot(x10, y10, marker='.', label='weight = 0.09')
plt.plot(x1, y1, marker='.', label='weight = 0.1')
plt.xlabel('Time Step')
plt.ylabel('Number of Different Words')
plt.title('Number of Different Words in Time')
plt.legend()
ax1.grid(True)
plt.show()
Y1=np.array(y1)
lastY1=y1[-1]
maxY1=Y1.max()
Y2=np.array(y2)
lastY2=y2[-1]
maxY2=Y2.max()
Y3=np.array(y3)
lastY3=y3[-1]
maxY3=Y3.max()
Y4=np.array(y4)
lastY4=y4[-1]
maxY4=Y4.max()
Y5=np.array(y5)
lastY5=y5[-1]
maxY5=Y5.max()
Y6=np.array(y6)
lastY6=y6[-1]
maxY6=Y6.max()
Y7=np.array(y7)
lastY7=y7[-1]
maxY7=Y7.max()
Y8=np.array(y8)
lastY8=y8[-1]
maxY8=Y8.max()
Y9=np.array(y9)
lastY9=y9[-1]
maxY9=Y9.max()
Y10=np.array(y10)
lastY10=y10[-1]
maxY10=Y10.max()
maxes=[maxY1,maxY2,maxY3,maxY4,maxY5,maxY6,maxY7,maxY8,maxY9,maxY10]
lasts=[lastY1,lastY2,lastY3,lastY4,lastY5,lastY6,lastY7,lastY8,lastY9,lastY10 ]
betaas=[0.1, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
plt.plot(betaas,lasts, marker='*', label='the last ndw')
plt.plot(betaas, maxes, marker='.', label='The max ndw')
plt.xlabel('Beta')
plt.ylabel('Number of different words')
plt.title('The maximum and last value of the number of different words as a function of the weight beta')
plt.legend()
plt.show()