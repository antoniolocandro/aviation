__author__ = 'Antonio.Locandro'
import math

OCA = 420
required_altitude = 500

ma_gradient=2.5
distance_mapt_soc=1.20

def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step

def increased_gradient():
    print "simulation increased gradient"
    for i in frange(2.5,5.5,.5):
        print i,math.ceil(round(((((required_altitude-OCA)/(i/100))/3.2808)/1852)+distance_mapt_soc,2)/0.1)/10

def simulation_altiude(start,end,step,gradient):
    print "simulation altitude"
    for i in frange(start,end+step,step):
        print gradient,i,math.ceil(round(((((i-OCA)/(gradient/100))/3.2808)/1852)+distance_mapt_soc,2)/0.1)/10

print simulation_altiude(500,1500,100,4.5)

print increased_gradient()