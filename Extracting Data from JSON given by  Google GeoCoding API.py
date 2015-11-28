import urllib
import json

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_198339.json'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

	info = json.loads(data)
	print info["comments"]["count"]
	sum = 0
	for item in info:
		sum=sum+int(item['comments']['count'])
	print sum


    