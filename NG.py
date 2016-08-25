#! /usr/bin/python

import random

from Agent import *
from Game import Play

#random.seed();

print "# GAME:"
folk = Folk(1000000,GRIDONMAP)
Play(folk,50000)

print folk

