__author__ = 'Antonio Locandro'
'''
Script only works for Central America FIR (FIR MHTG) due to hard coded values
'''

# import required modules
from shapely.geometry import Polygon
from geopy.distance import vincenty
from math import ceil

print "Calculating NOTAM radius of influence\n"

pl = Polygon([(-88.666667, 17.15), (-88.633333, 17.166667),(-88.65,17.133333)])

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

print 'NOTAM Coordinates and Radius\n%s%sE%03d'%(dd_dmsY(y)[0],dd_dmsX(x)[0],radius)
