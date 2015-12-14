# -*- coding: utf-8 -*-

from twx.botapi import TelegramBot, ReplyKeyboardMarkup, ReplyMarkup, ForceReply
import sys
import time
import requests
from StringIO import StringIO
import os,sys
import HTMLParser
#import Image


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
			print(data + " =====================================" )
			if(self.restaurant != ""):
				self.menu[self.restaurant] = self.foodlist
			self.restaurant = data
			self.foodlist = []

		if(self.in_pre):
			print(":::::::::::::" + data)
			self.foodlist.append(data)	
			#self.foodlist = data.split("\n")			
try:
	url = "https://wcdma-userarea.rnd.ki.sw.ericsson.se/ezivkoc/lunch.php"
	url = "http://dummy" # uncomment for non ECN test
	req = requests.get(url)

	req.encoding = 'utf-8'
	htmlText = req.text
	print req.encoding
	print htmlText

except requests.exceptions.ConnectionError:
	print "ConnectionError, failed to access https://wcdma-userarea.rnd.ki.sw.ericsson.se/ezivkoc/lunch.php"
	print "Will read menus from December 10 locally."
	htmlText = open("res/menus.html", "r").read()
	htmlText = str(htmlText)	

except:
	print " ===> other exception"
	e = sys.exc_info()[0]
	print e

#print(textEncode)

parser = FoodParser()
parser.feed(htmlText)
parser.close()
print("++++++++")
menu = parser.menu
for rest in menu:
	print "==============="
	print rest 
	for food in menu[rest]:
		print "-------" + food


