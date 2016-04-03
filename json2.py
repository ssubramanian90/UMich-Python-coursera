import urllib
import xml.etree.ElementTree as ET
import json



address = raw_input('Enter location: ')


url = address
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
sumcount=count=0
all={}
info = json.loads(str(data))
if info.has_key('comments'):
    for item in info.get('comments'):
        if item['name']!= ' ':
                count+=1
                sumcount+= int(item['count'])


print 'Count: '+str(count)
print 'Sum: '+str(sumcount)

