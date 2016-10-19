import matplotlib.pyplot as plt
import numpy as np

def tesplot(filename, delim='\t', skip=1):
	i, nw, ndw = np.loadtxt(filename, delimiter=delim, skiprows=skip, unpack=True)
	fig=plt.figure(figsize=(16,12))
	ax=plt.subplot(111)
	ax.spines["top"].set_visible(False)
	ax.spines["bottom"].set_visible(False)
	ax.spines["right"].set_visible(False)
	ax.spines["left"].set_visible(False)
	ax.get_xaxis().tick_bottom()
	ax.get_yaxis().tick_left()
	plt.tick_params(axis="both",
		which="both",
		bottom="off",
		top="off",
		labelbottom="on",
		left="off",
		right="off",
		labelleft="on")
	plt.plot(nw, label="Number of Words")
	plt.plot(ndw, label="Number of different Words")
	plt.legend()
	plt.show()

