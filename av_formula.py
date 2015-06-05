__author__ = 'Antonio.Locandro'

from math import *

def tas (ias,altitude,var):
    k = 171233
    c = (((288+var)-0.00198*(altitude/1000))**0.5)/(288-0.00198*(altitude/1000))**2.628

    print k,c


def rate_of_turn (tas,bank_angle):
    return (3431*tan(radians(bank_angle)))/(pi*tas)

print tas (250,7000,15)

print rate_of_turn(318.05,15)