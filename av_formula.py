# -*- coding: UTF-8 -*-
__author__ = 'Antonio.Locandro'

'''
Python module to make aviation conversions
'''

# import required modules
from math import *

'''
Aviation Calculations
'''

def tas_calculation (ias,altitude,var,bank_angle):
    k = 171233*(((288+var)-0.00198*altitude)**0.5)/(288-0.00198*altitude)**2.628
    tas = k*ias
    rate_of_turn = (3431*tan(radians(bank_angle)))/(pi*tas)
    radius_of_turn = tas/(20*pi*rate_of_turn)
    return k,tas,rate_of_turn,radius_of_turn

def wind_omni(altitude):
    w = (2*altitude/1000)+47
    return w

print tas_calculation(192,1000,15,15)
#print wind_omni(1000)


for i in range (0,180,30):
    windspiral = (i/0.8440760345564935)*(85.0/3600)
    print '%i,%s' % (i, windspiral)


