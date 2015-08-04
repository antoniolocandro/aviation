__author__ = 'Antonio.Locandro'
'''
Copyright (c) 2015 can't be used without authorization
'''
import os
from pykml import parser
import csv
import Tkinter
root = Tkinter.Tk()
root.withdraw()
from tkFileDialog import *


kml_file = askopenfilename(title="Radar Track KML file",initialfile='*.kml')

bname = os.path.splitext((os.path.basename(kml_file)))[0].rsplit('_dat',1)[0]
bpath = os.path.dirname(kml_file)
#print bname
#print bpath

#out = raw_input('Name for output file: ')+'.csv'
out = bpath+'/csv/'+bname +'.csv'

out_file = open(out,'wb')
csv_writer = csv.writer(out_file,quoting=csv.QUOTE_MINIMAL)

out_data = []

#kml_file = 'C://erase//tst//MCA200715_dat_kmlplot.kml'

root = parser.fromstring(open(kml_file,'r').read())

out_data.append('gid,time,radar_mode,aircraft_id,elevation_ft,none,longitude,latitude,elevation_m'.split(','))
count = 0

for e in root.Document.Folder.Folder.Placemark:
    for n in e.description:
        #print '%s,%s,%s,%s'%(n.text.split(',')[0],n.text.split(',')[1],n.text.split(',')[2],n.text.split(',')[4])
        #m = '%s,%s,%s,%s'%(n.text.split(',')[0],n.text.split(',')[1],n.text.split(',')[2],n.text.split(',')[4])
        count +=1
        #out_data.append(n.text.split(','))
    for m in e.Point.coordinates:
        #print m.text.split(',')
    #out_data.append(n+m)
        j = str(count)+','+n+','+m
        out_data.append(j.split(','))

for row in out_data:
    #print type(row)
    csv_writer.writerow(row)

out_file.close()

print "\nwrote %s with %s lines"%(out,count)