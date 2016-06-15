#! /usr/bin/python

import random

from Agent import *
from Game import Play

#random.seed();

print "# GAME:"

folk = Folk(500,GRIDONMAP)
Play(folk,10000000)

print folk

