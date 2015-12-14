__author__ = 'antonio.locandro'

'''
BaroVNAV scripts using DOC 8168 VOL II 6th Edition
'''
from math import log
from math import atan
from math import radians
from math import tan
from math import degrees
# Temperature Correction

def temperature_correction(Hthr,Hfap,ref_T,units):
    if units == "meters":
        delta_h=(((-6.5*(float(Hthr)/1000))+15-float(ref_T))/(-0.0065))*log(1+((-0.0065*float(Hfap-Hthr))/(288.15-0.0065*float(Hthr))))
        return delta_h
    elif units == "feet":
        delta_h=((((-6.5/3.2808)*(float(Hthr)/1000))+15-float(ref_T))/(-0.0065/3.2808))*log(1+(((-0.0065/3.2808)*float(Hfap-Hthr))/(288.15-(0.0065/3.2808)*float(Hthr))))
        return delta_h

Hthr=float(raw_input("Hthr? "))
Hfap=float(raw_input("Hfap? "))
ref_T=float(raw_input("ref_T? "))
units=raw_input("units? ")
distance_fap_thr = 4.7
rdh = 50
distance_fap_thr = float(raw_input("Distance FAP-MAPt (NM)? "))
att = 0.24
VPA = float(3.0)

delta_h = round(temperature_correction(Hthr,Hfap,ref_T,units),0)
print delta_h

def temperature_vpa(Hfap,Hthr,delta_h,rdh,distance_fap_thr):
    temperature_vpa = degrees(atan((((Hfap-Hthr-delta_h-rdh)/3.2808)/1852)/distance_fap_thr))
    return temperature_vpa

minVPA = temperature_vpa(Hfap,Hthr,delta_h,rdh,distance_fap_thr)
print minVPA

def xFAS():
    if Hfap < 5000:
        return (((75-50/3.2808)/1852)/tan(radians(VPA)))+att

def aFAS():
    if Hfap < 5000:
        return degrees(atan(((Hfap-Hthr-delta_h-75*3.2808)*tan(radians(VPA))/(Hfap-Hthr-75*3.2880))))


xFS =  xFAS()
print xFAS()
aFS = aFAS()
print aFAS()


def hFAS(x):
    return (x-xFS)*tan(radians(aFS))

print hFAS(3.34)*1852*3.2808+Hthr ,"hfas"

def intFAS(hFS):
    return (hFS/tan(radians(aFS)))+xFS

print intFAS((740.5912/3.2808)/1852)