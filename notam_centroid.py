__author__ = 'Antonio Locandro'
'''
Script only works for Central America FIR (FIR MHTG) due to hard coded values
'''

# import required modules
import os
import csv
import Tkinter
root = Tkinter.Tk()
root.withdraw()
from tkFileDialog import *

from shapely.geometry import Polygon
from geopy.distance import vincenty
from math import ceil
from shapely.wkt import dumps, loads


csv_file = askopenfilename(title="csv for radius of influence calculation",initialfile='*.csv')

cvr = "Polygon(("

with open(csv_file, 'rb') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csv_read, None)
    for row in csv_read:
        cvr+=""+row[9]+" "+row[8]+","

pl = loads (cvr.rstrip(",")+"))")

#debug print
#print pl

print "Calculating NOTAM radius of influence\n"

vl = pl.centroid

x = vl.x
y = vl.y


def dd_dmsX(dd):
    degrees = abs(int(dd))
    sub_minutes = int(round(abs(dd - int (dd))*60,0))
    nx = -(degrees+sub_minutes/60.0)
    return ('%03d%02dW' % (degrees, sub_minutes),nx)

def dd_dmsY(dd):
    degrees = abs(int(dd))
    sub_minutes = int(round(abs(dd - int (dd))*60,0))
    ny = (degrees+sub_minutes/60.0)
    return ('%02d%02dN' % (degrees, sub_minutes),ny)

y2=dd_dmsY(y)[1]
x2=dd_dmsX(x)[1]

counter = 0
rl = []
for v in list(pl.exterior.coords):
    cy = list(pl.exterior.coords)[counter][1]
    cx = list(pl.exterior.coords)[counter][0]
    counter += 1
    rl.append((vincenty((y2, x2),(cy, cx)).meters/1852.0))

radius = int(ceil(max(rl)))

print 'NOTAM Coordinates and Radius\n%s%s%03d'%(dd_dmsY(y)[0],dd_dmsX(x)[0],radius)
