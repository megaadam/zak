# -*- coding: utf-8 -*-

from random import randint

class Phrase:
	def __init__(self):

		self.nicks= {
		"Arturo": ["Arturo", "Artie", "Arturix", "R2", "artoooo", "Arturiño", "Diztroyer of Badness", "Destroyer of Badness", "Dooderiño", "Hombre", "Smarturo", "Zapata", "Zapatito", "mi amor"],
		"Gustav": ["Gustav", "Gus", "Gustavo", "Gus doood", "Gee One", "dude", "Mister", "Gus-man"],
		"Adamski": ["Adamski", "Adam", "Adamito", "Hungarian dude", "dood", "Mister", "Adamsson", "Adamiño"],
		"Diego": ["Diego", "D1", "Diegs", "Diegito", "Señor"]
		}

		self.dinners = [ 
		"For dinner, #nick#, I would recommend a 1972 Chateau de la Père et ses Frères",
		"Nah, just grab a beer if you get hungry dude.",
		"If you have chicken, may I suggest a light white Piemontese?",
		"Dinner? Really?? Isn't it a bit early for dinner mate?",
		"#nick#, for you, anything but fish",
		"I think you should focus on the the Belgo Chimays, #nick#!",
		"Well #nick#, I've heard the mussels at Belgo are pretty nice."]


	# the rnd methods could also be used for nicknames, restaurants etc
	def rnd(self, phrases):
		if(len(phrases) < 1):
			return ""
		return phrases[randint(0, len(phrases)-1)]

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
		return phrase.replace("#nick#", self.nick)

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
