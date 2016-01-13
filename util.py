# -*- coding: utf-8 -*-

from datetime import date, datetime


class Msg:
	def __init__(self, chatId, text, tokens, sender):
		self.chatId = chatId
		self.text = text
		self.tokens = tokens
		self.sender = sender
		self.nick = ""

# Wrap time for test hacks etc
class T:
	@staticmethod
	def dayOfWeek():
		dow = date.today().weekday()
		return dow

	@staticmethod
	def weekend():
		return T.dayOfWeek() > 4

	@staticmethod
	def weekday():
		wd = T.dayOfWeek()
		return {	
		0: "Monday",
		1: "Tuesday",
		2: "Wednesday",
		3: "Thursday, and cocktails tonite",
		4: "Friday at last!",
		5: "Saturday",
		6: "Sunday"
		}[wd]

	@staticmethod
	def year():
		h = datetime.now().year
		return h

	@staticmethod
	def month():
		h = datetime.now().month
		return h

	@staticmethod
	def day():
		d = datetime.now().day
		return d

	@staticmethod
	def hour():
		h = datetime.now().hour
		return h

	@staticmethod
	def minute():
		h = datetime.now().minute
		return h




