__author__ = 'Antonio.Locandro'

import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=gisdb user=locandro host=172.16.11.39 port=5433 password=alocandro34")

# txt parameterers
text_file = open('test_tma.csv', "wb")
text_file.write('polygon_id,polygon_vertex,lat,lon\n')

# Open a cursor to perform database operations
cur = conn.cursor()

# Query the database and obtain data as Python objects
cur.execute("SELECT path, ST_AsLatLonText(geom, 'D M S C') FROM (SELECT (ST_DumpPoints(geom)).* FROM ( SELECT * FROM gis20151015.tma)I)J;")
rows = cur.fetchall()

counter = 1
polygon = 1
for n in rows:
    w =n[1].split(' ')
    s =n[0][2]

    if s-counter <> 0:
        polygon += 1
        counter = 1
    counter+=1
        #print n
    dd_lat = float(w[0])
    mm_lat = float(w[1])
    ss_lat = float(w[2])
    hh_lat = w[3]
    dd_lon = float(w[4])
    mm_lon = float(w[5])
    ss_lon = float(w[6])
    hh_lon = w[7]

    #print polygon,s
    #print '%s,%s,%i %i %i %s,%i %i %i %s'%(polygon,s,dd_lat,mm_lat,ss_lat,hh_lat,dd_lon,mm_lon,ss_lon,hh_lon)
    lt = ('%i,%i,%i %i %i %s,%i %i %i %s\n'%(polygon,s,dd_lat,mm_lat,ss_lat,hh_lat,dd_lon,mm_lon,ss_lon,hh_lon))
    text_file.write(lt)
cur.close()
conn.close()