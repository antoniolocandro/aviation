import urllib2
import re
import csv
from bs4 import BeautifulSoup
AD = 'MROC'
#url= 'http://flightaware.com/live/flight/SWA827/history/20151213/2020Z/KHOU/MZBZ/tracklog'

url = raw_input('enter url  ')

page = urllib2.urlopen(url).read()


soup = BeautifulSoup(page,'html.parser')

flight_airline = soup.title.text.replace(u'\u2708',",").split(',')[1].strip(' ')
flight_date = soup.title.text.replace(u'\u2708',",").split(',')[2].strip(' ')
flight_destination = soup.title.text.replace(u'\u2708',",").split(',')[3].strip(' ').split('/')[1].strip(' ')

#^smallrow\d
table = soup.find_all("tr", { "class" : re.compile(r"^smallrow1|smallrow2")})

 #with open('eggs.csv', 'rb') as csvfile:
  #  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
bpath ="C://erase/antopy"
bname = flight_destination+'_'+flight_date+'_'+flight_airline

#out = bpath+'/'+AD+'/csv/'+bname +'.csv'
out = bpath+'/csv/'+bname +'.csv'

out_file = open(out,'wb')
csv_writer = csv.writer(out_file,quoting=csv.QUOTE_MINIMAL)

out_data = []
out_data.append('gid,time,Latitude,Longitude,Direction,KTS,MPH,Altitude_ft'.split(','))
count = 0

for row in table:
        cells = row.findAll('td')

        if len(cells) ==10 and cells[7].text.encode('utf-8') is not '':

            j = '%i,%s,%f,%f,%s,%f,%f,%s'%(count,cells[0].text.encode('utf-8'),float(cells[1].text.encode('utf-8')),float(cells[2].text.encode('utf-8')),cells[4].text.encode('utf-8'),float(cells[5].text.encode('utf-8')),float(cells[6].text.encode('utf-8')),float(cells[7].text.encode('utf-8').replace(',','')))

            print j
            out_data.append(j.split(','))
            count +=1
        else:
            pass
            #print cells[7].text

for row in out_data:
    csv_writer.writerow(row)


out_file.close()

print "\nwrote %s with %s lines"%(out,count)