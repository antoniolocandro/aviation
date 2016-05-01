# import modules
import psycopg2
import csv
# paths
dtm_path = "C://erase//osdtm//"

# Connect to an existing database
conn = psycopg2.connect("host= localhost dbname=uk user=postgres password=19835816")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("DROP TABLE IF EXISTS dtm.temp_msa;CREATE TABLE dtm.temp_msa (gid serial PRIMARY KEY, X float,Y float, HEIGHT float,dtm_id varchar);")
cur.execute("SELECT AddGeometryColumn ('dtm','temp_msa','geom',4326,'POINT',2);")

# Query the database and obtain data as Python objects
cur.execute("SELECT d.gid,d.os_grid_ref,d.geom from dtm.os_grid_ref d,msa_select m where st_INTERSECTS (d.geom,m.geom)")

list =[]

for row in cur:
    print row
    dt_path = dtm_path+row[1][:2].lower()+"//DTM_"+row[1]+".csv"
    list.append(dt_path)


for row in list:
    dt_path = row
    #print dt_path
    with open(dt_path, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        spamreader.next()
        for row in spamreader:
            if set(row).pop()=='':
                pass
            else:
                for n in row:
                    op = n.split(',')
                    print op[0],op[1],op[2],op[3]
                    #cur.execute("INSERT INTO dtm.temp_msa (X, Y,HEIGHT, dtm_id) VALUES (count,%s, %f,%f,%s)",n)
                    cur.execute("INSERT INTO dtm.temp_msa (X, Y,HEIGHT, dtm_id,geom) VALUES (%s, %s,%s,%s,ST_SetSRID(ST_MakePoint(%s,%s),4326))",(op[0],op[1],op[2],op[3],op[0],op[1]))
                    #cur.execute("Update dtm.temp_msa set geom= ST_SetSRID(ST_MakePoint(%s,%s),4326)",(op[0],op[1]))
                    #print "GEOMETRY"
    #print dtm_path+row[1][:2].lower()+"//DTM_"+row[1]+".csv"

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
#cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# Make the changes to the database persistent

    conn.commit()

# Close communication with the database
cur.close()
conn.close()

