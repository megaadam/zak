# -*- coding: utf-8 -*-


from parse import Menu
from phrases import Phrase
from datetime import datetime
from random import randint, shuffle
import re
import sys

msgTxt = 'toc toc,ton?ton!tic;tac.tix\ntox+tox¿tox-tox*tox/toz=tiz'
#msgTokens = re.split(' |,|;|.|:|!|?|¡|¿|+|-|*|/|=|"|\\', msgTxt)
tokens = re.split(',|;|!|\?|\.|\+|-|\*|/|=|¿|\s', msgTxt)
for t in tokens:
	print t
sys.exit(0)

m = Menu()
p = Phrase()
rests = m.getRestaurants()

for i in range(20):
	rest = p.rnd(rests)
	foods = m.getFoods(rest)
	food = p.rnd(foods)
	try:
		print u"At " + rest + u"\t eat " + food	

	except:
		print " ========> Decode exception : " + food

	if("?" in food):
		print "contains ?"

if(m.getLocalMode()):
	print "Running in local mode."
else:
	print "Online mode active"

print "URL is: " + m.getUrl()

print "Hour " + str(datetime.now().hour)