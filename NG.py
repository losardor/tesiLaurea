#! /usr/bin/python

import random

from Agent import *
from Game import Play
import numpy as np
import sys, getopt

def main(argv):
	outputfile = ''
	choice = 1
	beta=0.1
	try:
		opts, args = getopt.getopt(argv,"ho:c:t:b:",["ofile=","choice=","topology=","beta="])
	except getopt.GetoptError:
		print 'NG.py -o <outputfile> -c <choice> -t <topology>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print "NG.py -o <outputfile> -c <choice> -t <topology> -b <beta>",
			"\nfor choice the options are:\n0 for unweighted choice\n1 for weighted choice",
			"for topology the possibilities are NON MI INTERESSA ADESSO",
			"For beta interesting values are between 0.001 and 0.1"

			sys.exit()
		elif opt in ("-c", "--choice"):
			choice=arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-b", "--beta"):
			beta=float(arg)

	if outputfile == '':
		outputfile="gameBeta"+str(beta)+".dat"

	folk=Folk(800000, GRIDONMAP, choice = choice, Beta = beta)
	Play(folk, 1000000, name=outputfile)

if __name__=="__main__":
	main(sys.argv[1:])





























