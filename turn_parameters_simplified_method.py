__author__ = 'Antonio.Locandro'
'''
turn parameters for VOR and NDB Routes (Simplified Version)
'''

from math import pi

def enr_conventional_turn (altitude,turn_angle):


    radius_turn = 3431*turn_angle/(2*pi*R)

    wind = 2*altitude/1000+47

    return altitude, turn_angle, wind,radius_turn


print enr_conventional_turn(19000,27.20981998)