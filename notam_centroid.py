__author__ = 'Antonio Locandro'

'''
Script only works for Central America FIR (FIR MHTG) due to hard coded values
'''

# import required modules
from geographiclib import geodesic
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
import webbrowser

csv_file = askopenfilename(title="csv for radius of influence calculation",initialfile='*.csv')

cvr = "Polygon(("
notam_line = []

with open(csv_file, 'rb') as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csv_read, None)
    for row in csv_read:
        cvr+=""+row[9]+" "+row[8]+","
        notam_line.append((float(row[8]),float(row[9])))
pl = loads (cvr.rstrip(",")+"))")
#notam_line = notam_line.rstrip(",")

#print notam_line

#debug print
#print pl

print "Calculating NOTAM radius of influence\n"

vl = pl.centroid

x = vl.x
y = vl.y

#debug print
#print x,y


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


'''
circle calculation
'''
cnotam = []
def circle(lat,lon):

    for i in range(0,360,1):
        result=geodesic.Geodesic.WGS84.Direct(lat, lon, i, radius*1852)
        lat2, lon2 = result["lat2"], result["lon2"]
        cnotam.append((lat2,lon2))
        #debug print
        #print lat2,lon2

circle(y2,x2)
#print cnotam


'''
visualization
'''

import folium
map_osm = folium.Map(location=[y, x],zoom_start=12)
map_osm.circle_marker(location=[y, x], radius=100,
                  popup='Calculated Centroid', line_color='#3186cc',
                  fill_color='#3186cc', fill_opacity=0.2)
map_osm.simple_marker ([y2, x2],popup='NOTAM Centroid and Radius of Influence\n%s%s%03d'%(dd_dmsY(y)[0],dd_dmsX(x)[0],radius))
#print notam_line
map_osm.line(notam_line, line_color='#FF0000', line_weight=3)
map_osm.line(cnotam, line_color='#3186cc', line_weight=10)
map_osm.create_map(path='C:\\Users\\antonio.locandro\\Desktop\\notam_radius.html')

url = "C:\\Users\\antonio.locandro\\Desktop\\notam_radius.html"
webbrowser.get().open(url,new=1)