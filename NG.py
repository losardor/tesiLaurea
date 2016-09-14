#! /usr/bin/python

import random

from Agent import *
from Game import Play
import numpy as np

#random.seed();

print "# GAME:"
#GAME1
for i in range(10):
	beta = (i+1.0)/100
	folk=Folk(8000, GRIDONMAP, choice = 1, Beta = beta)
	folk.agent[0].ndw=0
	folk.agent[0].nw = 0
	folk.agent[0].words = []
	Play(folk, 100000, name="gameBeta"+str(beta)+".dat")