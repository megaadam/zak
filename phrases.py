# -*- coding: utf-8 -*-

from random import randint, shuffle
from util import T, Msg

class Phrase:
	def __init__(self):

		self.phraseHistory = {}
		self.nicks = {
		"Arturo": ["Arturo", "Artie", "Arturix", "R2", "artoooo", u"Arturiño", "Diztroyer of Badness", "Destroyer of Badness", u"Dooderiño", "Hombre", "Smarturo", "Zapata", "Zapatito", "mi amor"],
		"Gustav": ["Gustav", "Gus", "Gustavo", "Gus doood", "Gee One", "dude", "Mister", "Gus-man"],
		"Adamski": ["Adamski", "Adam", "Adamito", "Hungarian dude", "dood", "Mister", "Adamsson", u"Adamiño"],
		"Diego": ["Diego", "D1", "Diegs", "Diegito", u"Señor"] # Diego is the only true Señor
		}

		self.greeting1 =[
		"Hi #nick# and everybody",
		"Doodz! Really awesome to see you!!",
		"Greetings friends. Is it really #weekday# already?",
		"#nick# man! Are you happy that it's #weekday#?"]

		self.greeting2 = [
		"sup?",
		"What's going on over there?",
		"you OK?",
		"What else is new?",
		"Any news?",
		"So who is leaving HSS this week then?"]

		self.hiArturo = [
		u"Eyy muchaco! ¿Que Pasa?",
		"Hi #nick#! \nHowz Madrid?\nCold in December eh?",
		"Hey! Are you still in Madrid?",
		"toc toc"]

		self.dinners = [ 
		"For dinner, #nick#, I would recommend a 1972 Chateau de la Père et ses Frères",
		"Forget dinner #nick#!! Have a tripple Carolina instead.",
		"Nah, just grab a beer if you get hungry dude.",
		"If you have chicken, may I suggest a light white Piemontese?",
		"Dinner? Really?? Isn't it a bit early for dinner mate?",
		"#nick#, for you, anything but fish",
		"I think you should focus on the the Belgo Chimays, #nick#!",
		"Well #nick#, I've heard the mussels at Belgo are pretty nice."]

		self.restIntro = [
		"From the the top of my head #nick#, I know ",
		"#nick#, the places I know are: "]

		self.restAnd = [
		"and ", "but also ", "plus ", "and finally ", "... I alomost forgot: ", "and last but not least ", "alternatively ", 
		"unless you prefer ", "but this one is ok too: ", "or you could try"]

		self.sweResp = ["Sorry, my Swedish is not so good. But I can reply...", 
		u"Orrschakta, minn svanske er jette gansk dålig? ",
		"Is that Swedish? I know noothing. I come from Barcelona.",
		"Sorry buddy, no habla sueco!",
		"Would you please speak English, Sir?",
		"How many languages dya think I speak #nick#?"
		]

		self.breakf = [ 
		"I'm not much for breakfast. I like to sleep instead.",
		"Not my kind of thing, dude.",
		"Breakfast? You gotta be kidding!",
		"You know me #nick#! I not a breakfast kinda guy."
		"Nah, breakfast is for idiots, I eat CPU cycles.",
		"Just black coffe, thank you."]

		self.artLunch = [
		"I though you were in Spain #nick#, why dontcha ask your mum?",
		"You could ask your mother to cook for you #nick#. She is in the next room isn't she?",
		"Ah these Peruvian dudes! If you are in Barcelo\nsorry Madrid\nyou COULD ask your mummy, yeah?",
		"I cant help you.\nYou are in Madrid."]

		self.glaze = [
		"I agree #nick# that's the best place in Kista. Too bad they don't post their menus.",
		"I was human I would go to Glaze every day!",
		"Glaze is not to bad I guess, for a restaurant in a dump like Kista...",
		"I wish there were more places like Glaze, sorry but I cannot read their menus."]

		self.zack1 = [
		"Listen #nick#.",
		"#nick#..."]

		self.zack2 =  ["My name is Zak.", "You should know my name by now, it's: Zak",
		"The name is Zak, buddy.", "Don't you ever forget, they call me Zak."]


		self.helga = [
		u"Helgafjäll", "Refactory", "reefactoree", "Un-fac-tory", "Unfactory", "Helga"]

		self.restNicks = list(self.helga) # make a copy!
		self.restNicks.append(["HK", "Micro", "Thai", "World"])


	# the rnd methods could also be used for nicknames, restaurants etc
	def rnd(self, phrases):
		if(len(phrases) < 1):
			return ""

		if(len(phrases)==1):
			return phrases[0]

		key = phrases[0]
		if(key not in self.phraseHistory):
			i = randint(0, len(phrases)-1)
		else:
			while(True):
				i = randint(0, len(phrases)-1)	
				if i != self.phraseHistory[key]:
					break

		self.phraseHistory[key] = i
		return phrases[i]
			
	def fixAliasOld(self, phrase):
		resp = phrase
		resp = resp.replace(u"#nick#", self.nick)
		hel = self.rnd(self.helga)
		resp = resp.replace(u"Helgafjäll", hel)
		return resp

	def fixAlias(self, phrase, msg):
		resp = phrase
		if(msg.nick == ""):
			# No override use defaults
			nick = self.nickname(msg.sender)
		else:
			nick = msg.nick

		helgaNick = self.rnd(self.helga)
		resp = resp.replace(u"#nick#", nick)
		resp = resp.replace(u"#weekday#", T.weekday())
		resp = resp.replace(u"Helgafjäll", helgaNick)
		return resp

	def nickname(self, name):
		if(name in self.nicks):
			nix = self.nicks[name]
			theNick = self.rnd(nix)
			return theNick
		else:
			return name

########################################################################################
##	the vocab
	def getGreeting1(self, msg):
		return self.fixAlias(self.rnd(self.greeting1), msg)

	def getGreeting2(self, msg):
		return self.fixAlias(self.rnd(self.greeting2), msg)

	def getHiArturo(self, msg):
		return self.fixAlias(self.rnd(self.hiArturo), msg)

	def getZack1(self, nick):
		self.nick = nick
		return self.fixAliasOld(self.rnd(self.zack1))

	def getZack2(self, nick):
		self.nick = nick
		return self.fixAliasOld(self.rnd(self.zack2))

	def getArtLunch(self, msg):
		self.nick = self.nickname(msg.sender)
		print self.nick
		return self.fixAliasOld(self.rnd(self.artLunch))

	def dinner(self, nick):
		self.nick = nick
		return self.fixAliasOld(self.rnd(self.dinners))

	def getGlaze(self, nick):
		self.nick = nick
		return self.fixAliasOld(self.rnd(self.glaze))

	def swedish(self, nick):
		self.nick = nick
		resp = self.rnd(self.sweResp)
		resp = self.fixAliasOld(resp)
		return resp

	def breakfast(self, nick):
		self.nick = nick
		resp = self.rnd(self.breakf)
		resp = self.fixAliasOld(resp)
		return resp

	def restaurants(self, nick, r):
		self.nick = nick
		if len(r) < 1:
			return self.fixAliasOld("Restaurant databaze error, sorry #nick#.")
		resp = self.rnd(self.restIntro)
		for i in range(len(r)-2):
			resp += r[i]
			if(i < len(r)-2):
				resp += ", "

		resp += self.rnd(self.restAnd)
		resp += r[len(r)-1]
		resp += "."
		resp = self.fixAliasOld(resp)
		return resp

