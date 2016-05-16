#! /usr/bin/python

import random

from Agent import *
from Game import Play

#random.seed();

print "# GAME:"

folk = Folk(100,GRID2DBAND)
Play(folk,1000000)

print folk

