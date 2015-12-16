# -*- coding: utf-8 -*-

import sys
import requests
import HTMLParser
from random import randint

class FoodParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.in_h3 = False
		self.in_pre = False
		self.restaurant = ""
		self.foodlist = []
		self.menu = {}

	def handle_starttag(self, tag, attrs):
		if(tag=="h3"):
			self.in_h3 = True

		if(tag=="pre"):
			self.in_pre = True


	def handle_endtag(self, tag):
		if(tag=="h3"):
			self.in_h3 = False

		if(tag=="pre"):
			self.in_pre = False

	def handle_data(self, data):
		if self.in_h3:
			self.restaurant = data

		if(self.in_pre):
			self.menu[self.restaurant] = data.split('\n')

class Menu:
	def __init__(self):
		self.url = "https://wcdma-userarea.rnd.ki.sw.ericsson.se/ezivkoc/lunch.php"
		self.localmode = False
		self.retrieveMenu()
		self.ignorelist=["Boscherian"]

	def retrieveMenu(self):				
		try:
			
			#self.url = "http://dummy" # uncomment for non ECN test
			req = requests.get(self.url)

			req.encoding = 'utf-8'
			htmlText = req.text
			print req.encoding
			print htmlText

		except requests.exceptions.ConnectionError:
			self.localmode = True
			print "Invoking local mode"
			htmlText = open("res/menus.html", "r").read()
			htmlText = str(htmlText)	

		except:
			print " ===> other exception"
			e = sys.exc_info()[0]
			print e

		parser = FoodParser()
		parser.feed(htmlText)
		parser.close()
		print("++++++++")
		self.menu = parser.menu

	def getMenu(self):	
		return self.menu

	def rndRest(self):
		while True:
			rest = self.menu.keys()[randint(0, len(self.menu)-1)]
			if rest not in self.ignorelist:
				break
		return rest

	def rndFood(self, rest):
		if rest not in self.menu.keys():
			return ""

		foodz = self.menu[rest]
		if len(foodz) == 0:
			return ""

		return foodz[randint(0, len(foodz)-1)]	

	def getLocalmode(self):
		return self.localmode

	def getUrl(self):
		return self.url




