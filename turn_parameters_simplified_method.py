__author__ = 'Antonio.Locandro'
'''
turn parameters for VOR and NDB Routes (Simplified Version)
'''

#from math import pi
from av_formula import *

print tas_calculation(315,14763.6,15,15)

def enr_conventional_turn (turn_angle):
    kk_dist = tas_calculation(315,14763.6,15,15)[3]*tan(radians(turn_angle/2))
    print kk_dist

print tas_calculation(315,14763.6,15,15)[3]*1852

enr_conventional_turn(27.20981998)