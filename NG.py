#! /usr/bin/python

import random

from Agent import *
from Game import Play

#random.seed();

print "# GAME:"
folk = Folk(1000,GRIDONMAP)
Play(folk,10000)

print folk

