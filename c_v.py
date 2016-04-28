from geographiclib.geodesic import Geodesic

#declare runway thresholds

thr_lat_1= raw_input("latitude THR 1").upper()
thr_lon_1= raw_input("longitude THR 1").upper()
thr_lat_2= raw_input("latitude THR 2").upper()
thr_lon_2= raw_input("longitude THR 1").upper()

#declare ARP

#conversion dd to dms
def cnv(x):
    ab = x.split()
    if ab[3]=='N':
        conv = float(ab[0])+float(ab[1])/60.0+float(ab[2])/3600.0
        return conv
    elif ab[3]=='W':
        conv = -1.0*(float(ab[0])+float(ab[1])/60.0+float(ab[2])/3600.0)
        return conv
    else:
        print "idiot"

#inverse

print Geodesic.WGS84.Inverse(cnv(thr_lat_1),cnv(thr_lon_1),cnv(thr_lat_2),cnv(thr_lon_2))

