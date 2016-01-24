import json, httplib, urllib

conn = httplib.HTTPConnection("reisapi.ruter.no")
conn.request("GET","/Place/GetStopsRuter/")
content=conn.getresponse()
data=content.read()
jDict = json.loads(data)
for i in enumerate(jDict):
	Name = (i[1]['Name']).encode('ascii', 'ignore')
	ID = i[1]['ID']
	print Name," ",ID

