import json, httplib, urllib, time, datetime, digit
from sense_hat import SenseHat
import errno
from socket import error as socket_error

sense = SenseHat()
# Depends on which direction you place your Pi
sense.set_rotation(180)

# Change these for your ID
Origin="3012430" # Station ID for Hovseter T
Destination="3010011" # Station ID for Jernbanetorget T

conn = httplib.HTTPConnection("reisapi.ruter.no")
while True:
	currenttime=time.strftime("%d%m%Y%H%M%S")
	try: 
		# Connection is being held, not sure if wise
		conn.request("GET","/Travel/GetTravels?fromPlace="+
			Origin+"&toPlace="+
			Destination+"&isafter=True&time="+
			currenttime)
		content=conn.getresponse()
		data=content.read()
	except socket_error as serr: 
		if serr.errno != 104:
			raise serr
		else:
			# reconnect if connection is dropped
			conn.close(),
			conn = httplib.HTTPConnection("reisapi.ruter.no")
	# Parse returned data into Dictionary object
	jDict = json.loads(data)
	er = jDict['ReisError']
	if er==None:
		# Gets first proposal neares in time
		tt = jDict['TravelProposals'][0]['DepartureTime']
		# Some arithmetic to figure out minutes until departure
		current=datetime.datetime.strptime(currenttime,"%d%m%Y%H%M%S")
		next=datetime.datetime.strptime(tt,"%Y-%m-%dT%H:%M:%S")
		diff = next-current
		diffmin = (diff.days * 24 * 60) + (diff.seconds/60)
		# Don't need this fancy digit thing but easier to read
		sense.set_pixels(digit.makedigit(diffmin))
	else:
		print(er)
	## Be nice to the API servers
	time.sleep(10)

