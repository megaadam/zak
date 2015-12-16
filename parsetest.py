from parse import Menu
from datetime import datetime

m = Menu()
for i in range(10):
	rest = m.rndRest()
	food = m.rndFood(rest)
	try:
		food = food.decode('latin1')
		rest = rest.decode('latin1')
		print u"At " + rest + u"\t eat " + food	

	except:
		print " ========> Decode exception : " + food

	if("?" in food):
		print "contains ?"

if(m.getLocalmode()):
	print "Running in local mode."
else:
	print "Online mode active"

print "URL is: " + m.getUrl()

print "Hour " + str(datetime.now().hour)