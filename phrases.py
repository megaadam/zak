# -*- coding: utf-8 -*-

from random import randint, shuffle

class Phrase:
	def __init__(self):

		self.phraseHistory = {}
		self.nicks= {
		"Arturo": ["Arturo", "Artie", "Arturix", "R2", "artoooo", u"Arturiño", "Diztroyer of Badness", "Destroyer of Badness", u"Dooderiño", "Hombre", "Smarturo", "Zapata", "Zapatito", "mi amor"],
		"Gustav": ["Gustav", "Gus", "Gustavo", "Gus doood", "Gee One", "dude", "Mister", "Gus-man"],
		"Adamski": ["Adamski", "Adam", "Adamito", "Hungarian dude", "dood", "Mister", "Adamsson", u"Adamiño"],
		"Diego": ["Diego", "D1", "Diegs", "Diegito", u"Señor"] # Diego is the only true Señor
		}

		self.dinners = [ 
		"For dinner, #nick#, I would recommend a 1972 Chateau de la Père et ses Frères",
		"Forget dinner #nick#!! Have a tripple Carolina instead."
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
		"Is that Swedish? I know noothing. I come from Barcelona."
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

		self.helga = [
		u"Helgafjäll", "Refactory", "reefactoree", "Un-fac-tory", "Unfactory", "Helga"]

		self.restNicks = list(self.helga) # make a copy!
		self.restNicks.append(["HK", "Micro", "Thai", "World"])


	# the rnd methods could also be used for nicknames, restaurants etc
	def rnd(self, phrases):
		if(len(phrases) < 1):
			return ""

#		if(phrases not in self.phraseHistory):
#			shuffle(phrases)
#			i = randint(0, len(phrases)-1)
#		else:
#			i = (self.phraseHistory[phrases] + 1) % len(phrases)

		i = randint(0, len(phrases)-1)
		#self.phraseHistory[phrases] = i
		return phrases[i]

	def rndExcept(self, phrases, phrase):
		if(len(phrases) < 1):
			return ""

		if(len(phrases) == 1):
			return phrases[0]

		while(True):
			r = rnd()
			if(r != phrase):
				return r
			
	def fixAlias(self, phrase):
		resp = phrase
		resp = resp.replace(u"#nick#", self.nick)
		hel = self.rnd(self.helga)
		print hel
		resp = resp.replace(u"Helgafjäll", hel)
		return resp

	def nickname(self, name):
		if(name in self.nicks):
			nix = self.nicks[name]
			theNick = self.rnd(nix)
			return theNick
		else:
			return name

	def dinner(self, nick):
		self.nick = nick
		return self.fixAlias(self.rnd(self.dinners))

	def swedish(self, nick):
		self.nick = nick
		resp = self.rnd(self.sweResp)
		resp = self.fixAlias(resp)
		return resp

	def breakfast(self, nick):
		self.nick = nick
		resp = self.rnd(self.breakf)
		resp = self.fixAlias(resp)
		return resp

	def restaurants(self, nick, r):
		self.nick = nick
		if len(r) < 1:
			return self.fixAlias("Restaurant databaze error, sorry #nick#.")
		resp = self.rnd(self.restIntro)
		for i in range(len(r)-2):
			resp += r[i]
			if(i < len(r)-2):
				resp += ", "

		resp += self.rnd(self.restAnd)
		resp += r[len(r)-1]
		resp += "."
		resp = self.fixAlias(resp)
		return resp

