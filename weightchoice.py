import pandas as pnd
import numpy as np
from matplotlib import pyplot as plt
import random as rnd
PESO = 0.007
BINS=30
x, y = np.loadtxt('node_height', delimiter='\t', unpack=True)
heights = pnd.Series(y)
heights.hist(bins=BINS)
plt.show()
deltaH=[]
for i in range(1175):
	deltaH.append(abs(heights[rnd.randint(0,len(heights)-1)]-heights[rnd.randint(0,len(heights)-1)]))
DeltaH=pnd.Series(deltaH)
DeltaH.hist(bins=BINS)
plt.show()
weights=[]
for i in range(1175):
	weights.append(2.7**(-PESO*abs(heights[rnd.randint(0,len(heights)-1)]-heights[rnd.randint(0,len(heights)-1)])))
	if weights[i]<0:
		print weights[i]
Weight=pnd.Series(weights)
Weight.hist(bins=BINS)
plt.show()
print(max(Weight))
