import urllib2
import re
import csv
from bs4 import BeautifulSoup


def replaceMultiple (mainString,toBeReplaces,newString):
    for elem in toBeReplaces:
        if elem in mainString:
            mainString = mainString.replace(elem, newString)

    return mainString


AD = 'MGPB'
#url= 'http://flightaware.com/live/flight/SWA827/history/20151213/2020Z/KHOU/MZBZ/tracklog'

url = raw_input('enter url  ')

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page,'html.parser')

#print soup.title.text

flight_airline = soup.title.text.replace(u'\u2708',",").split(',')[1].strip(' ')
#flight_airline = 'N17WG'
flight_date = soup.title.text.replace(u'\u2708',",").split(',')[2].strip(' ')
#print flight_date
#flight_date = 'nil'
flight_destination = soup.title.text.replace(u'\u2708',",").split(',')[3].strip(' ').split('/')[1].strip(' ')
#flight_destination = 'nil'
#print flight_destination

#^smallrow\d
table = soup.find_all("tr", { "class" : re.compile(r"^smallrow1|smallrow2")})
print table
 #with open('eggs.csv', 'rb') as csvfile:
  #  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
bpath ="C://erase/antopy"
#bname = flight_destination+'_'+flight_date+'_'+flight_airline
bname = flight_date+'_'+flight_airline

out = bpath+'/'+AD+'/csv/2018/ref/'+bname +'.csv'
#out = bpath+'/csv/'+bname +'.csv'

out_file = open(out,'wb')
csv_writer = csv.writer(out_file,quoting=csv.QUOTE_MINIMAL)

out_data = []
out_data.append('gid,time,Latitude,Longitude,Direction,KTS,MPH,Altitude_ft,Rate_fpm'.split(','))
count = 0

for row in table:
        #print row
        cells = row.findAll('td')
        #print len(cells)

        if len(cells) ==10 and cells[7].text.encode('utf-8') is not '':

            j = '%i,%s,%f,%f,%s,%s,%s,%s'%(count,cells[0].text.encode('utf-8'),float(cells[1].text.encode('utf-8')[:7]),float(cells[2].text.encode('utf-8')[:8]),cells[4].text.encode('utf-8'),(cells[5].text.encode('utf-8')),(cells[6].text.encode('utf-8')),float(cells[7].text.encode('utf-8').replace(',','')[:len(cells[7].text.encode('utf-8'))/2]))

            #print j
            out_data.append(j.split(','))
            count +=1
        elif len(cells) ==9 and cells[7].text.encode('utf-8') is not '':
            #print 0,cells[0].text.encode('utf-8')
            #print 1,cells[1].text.encode('utf-8')[:7]
            #print 2,cells[2].text.encode('utf-8')[:8]
            #print 3,replaceMultiple(cells[3].text.encode('utf-8'),['&searr;','rarr;','nerr;','&deg;'],"")
            #print 4,cells[4].text.encode('utf-8')
            #print 6,float(cells[6].text.encode('utf-8').replace(",","."))*1000
            #print 7,cells[7].text.encode('utf-8')
            #print ''

            #j = '%i,%s,%f,%f,%s,%s,%s,%s'%(count,cells[0].text.encode('utf-8'),float(cells[1].text.encode('utf-8')[:7]),float(cells[2].text.encode('utf-8')[:8]),cells[4].text.encode('utf-8'),(cells[5].text.encode('utf-8')),(cells[6].text.encode('utf-8')),float(cells[7].text.encode('utf-8').replace(',','')[:len(cells[7].text.encode('utf-8'))/2]))
            j = '%i,%s,%f,%f,%s,%s,%s,%s,%s' % (count, cells[0].text.encode('utf-8'), float(cells[1].text.encode('utf-8')[:7]),float(cells[2].text.encode('utf-8')[:8]),replaceMultiple(cells[3].text.encode('utf-8'),['\xc2','\xe2','\xC3','\xC2','&searr;','&rarr;','&nearr;','&swarr','&nwarr','&deg;'],""), cells[4].text.encode('utf-8'), (cells[5].text.encode('utf-8')),float(cells[6].text.encode('utf-8').replace(",","."))*1000,replaceMultiple(cells[7].text.encode('utf-8'),[',','\xc2','\xe2','\xC3','\xC2'],""))

            #print j
            out_data.append(j.split(','))
            count +=1
        else:
            pass
            #print cells[7].text
            #print "2"

for row in out_data:
    csv_writer.writerow(row)


out_file.close()

print "\nwrote %s with %s lines"%(out,count)