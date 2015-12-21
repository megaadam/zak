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
		self.reloadMenu()
		self.ignorelist=["Boscherian"]

	def reloadMenu(self):				
		try:
			
			#self.url = "http://dummy" # uncomment for non ECN test
			req = requests.get(self.url)

			req.encoding = 'utf-8'
			htmlText = req.text

		except requests.exceptions.ConnectionError:
			self.localmode = True
			print "Invoking local mode"
			htmlText = open("res/menus.html", "r").read()
			htmlText = htmlText.decode('latin1')

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

	def getRestaurants(self):
		return self.menu.keys()

	def getFoods(self, rest):
		return self.menu[rest]

	def getLocalMode(self):
		return self.localmode

	def getUrl(self):
		return self.url
