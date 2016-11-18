#! /usr/bin/python

import random

from Agent import *
from Game import Play
import numpy as np
import sys, getopt

def main(argv):
	outputfile = ''
	choice = 1
	beta=0.05
	prob=1
	time=40000000
	try:
		opts, args = getopt.getopt(argv,"ho:c:t:b:p:",["ofile=","choice=", "time=","beta=","prob="])
	except getopt.GetoptError:
		print 'NG.py -o <outputfile> -c <choice> -t <time> -p <probability>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print "NG.py -o <outputfile> -c <choice> -t <time> -b <beta>",
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
		elif opt in ("-p", "--prob"):
			prob=float(arg)
		elif opt in ("-t", "--time"):
			time=float(arg)

	if outputfile == '':
		outputfile="gameBeta"+str(beta)+"Prob"+str(prob)+".dat"

	folk=Folk(10000, GRIDONMAP, choice = choice, Beta = beta)
	Play(folk, time, name=outputfile, prob=prob)

if __name__=="__main__":
	main(sys.argv[1:])





























