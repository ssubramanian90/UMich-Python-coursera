import urllib
import xml.etree.ElementTree as ET




address = raw_input('Enter location: ')


url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)
sumcount=count=0

counts = tree.findall('.//count')
for i in counts:
      count+=1
      sumcount+= int(i.text)
print 'Count: '+str(count)
print 'Sum: '+str(sumcount)
