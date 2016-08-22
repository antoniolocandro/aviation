import fiona
import math
from shapely.geometry import mapping, Polygon
from shapely.wkt import loads
from shapely.geometry import MultiLineString
import shapely.geometry
from shapely.ops import linemerge
import Tkinter
root = Tkinter.Tk()
root.withdraw()
from tkFileDialog import *

#url = "L:\\OTROS\\2016\\00031_cesar_nunez_guatemala\\shp\\IAP\\VOR_Y_RWY20.shp"
url = askopenfilename(title="Procedure",initialfile='*.shp')

source = fiona.open(url,"r")
t =  url.split('\\')
ext_name =  t[len(t)-1].replace('.shp','_procedure').upper()

# get shapefile extent
shape = source.bounds

x1 = shape[0]
y1 = shape[1]
x2 = shape[2]
y2 = shape[3]

poly_text = 'POLYGON (({0} {1},{0} {3},{2} {3},{2} {1},{0} {1}))'.format(x1,y1,x2,y2)

#print poly_text

poly_extent =loads(poly_text)

#print poly_extent

# Define a polygon feature geometry with one attribute
schema = {
    'geometry': 'Polygon',
    'properties': {'id': 'int'},
}

# Write a new Shapefile
with fiona.open(''+ext_name+'_extent.shp', 'w', 'ESRI Shapefile', schema) as c:
    ## If there are multiple geometries, put the "for" loop here
    c.write({
        'geometry': mapping(poly_extent),
        'properties': {'id': 1},
    })

def dd_to_dms(degs):
    neg = degs < 0
    degs = (-1) ** neg * degs
    degs, d_int = math.modf(degs)
    mins, m_int = math.modf(60 * degs)
    secs        =           60 * mins
    return neg, d_int, m_int, secs

#f = open("L:\\OTROS\\2016\\00031_cesar_nunez_guatemala\\map\\MGGT_"+ext_name+".map","w")
f = open(""+ext_name+".map","w")

print "Titulo Mapa        %s \n\n" \
      "/*   \n      NAMES FIJOS      \n" \
      "     =======================\n*/\n" \
      "ColorTexto            255 33 00\n\n" \
      "Rango                1024\n\n\n" \
      "/*\n    " \
      "         SYMBOLS FIJOS\n" \
      "         =======================\n*/\n" \
      "ColorSimbolos         255 33 00\n" \
      "Rango                1024\n/" \
      "*\n              %s\n" \
      "             ==============\n*/\n" \
      "Trazado     0\n" \
      "ColorLinea            255 33 00\n" \
      "Rango                1024\n"%(ext_name,ext_name)

f.write ("Titulo Mapa        %s \n\n" \
      "/*   \n      NAMES FIJOS      \n" \
      "     =======================\n*/\n" \
      "ColorTexto            255 33 00\n\n" \
      "Rango                1024\n\n\n" \
      "/*\n    " \
      "         SYMBOLS FIJOS\n" \
      "         =======================\n*/\n" \
      "ColorSimbolos         255 33 00\n" \
      "Rango                1024\n/" \
      "*\n              %s\n" \
      "             ==============\n*/\n" \
      "Trazado     0\n" \
      "ColorLinea            255 33 00\n" \
      "Rango                1024\n"%(ext_name,ext_name))



for s in source:
    #print s
    c_s = s['geometry']['coordinates']
    #print len(c_s)
    print '\nPolilinea %s [id_%s]'%(len(c_s),s['id'])
    f.write('\nPolilinea %s [id_%s]\n' % (len(c_s), s['id']))
    for i in c_s:
        print '%02i%02i%02iN%03i%02i%02iW'%(dd_to_dms(i[1])[1],dd_to_dms(i[1])[2],dd_to_dms(i[1])[3],dd_to_dms(i[0])[1],dd_to_dms(i[0])[2],dd_to_dms(i[0])[3])
        f.write('%02i%02i%02iN%03i%02i%02iW\n'%(dd_to_dms(i[1])[1],dd_to_dms(i[1])[2],dd_to_dms(i[1])[3],dd_to_dms(i[0])[1],dd_to_dms(i[0])[2],dd_to_dms(i[0])[3]))

f.close()