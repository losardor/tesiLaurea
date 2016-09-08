#! /usr/bin/python

import random

from Agent import *
from Game import Play
import numpy as np

#random.seed();

print "# GAME:"

#GAME1
folk=Folk(1000, GRIDONMAP, choice = 1)
Play(folk, 1000000, name="gameBeta.dat")


