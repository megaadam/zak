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



	def handle_starttag(self, tag, attrs):
		if(tag=="h3"):
			#print(tag)
			self.in_h3 = True

		if(tag=="pre"):
			self.in_pre = True



	def handle_endtag(self, tag):
		if(tag=="h3"):
			#print("--", tag)
			self.in_h3 = False

		if(tag=="pre"):
			self.in_pre = False



	def handle_data(self, data):
#		print("Data: ", data)
		if self.in_h3:
			print(str(data) + " =====================================" )

		if(self.in_pre):
			print(data)				

req = requests.get("https://wcdma-userarea.rnd.ki.sw.ericsson.se/ezivkoc/lunch.php")
textRaw = req.text
textEncode = textRaw.encode('utf-8')

#print(textEncode)

parser = FoodParser()
parser.feed(textEncode)
parser.close()
