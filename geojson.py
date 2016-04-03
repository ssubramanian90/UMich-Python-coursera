import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = raw_input('Enter location: ')
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None



pid = js["results"][0]["place_id"]
print 'Place id ',pid


