#! /usr/bin/python

import random

from Agent import *
from Game import Play

#random.seed();

print "# GAME:"
folk = Folk(8000,GRIDONMAP)
Play(folk,100000)

print folk

