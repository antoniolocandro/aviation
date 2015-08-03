__author__ = 'Antonio.Locandro'
'''
Copyright (c) 2015 can't be used without authorization
'''

from pykml import parser

kml_file = 'C://erase//tst//MCA200715_dat_kmlplot.kml'

root = parser.fromstring(open(kml_file,'r').read())

print 'time,radar_mode,aircraft_id,elevation_ft,none'

for e in root.Document.Folder.Folder.Placemark:
    for n in e.description:
        print n
