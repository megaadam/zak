# -*- coding: utf-8 -*-
# Please do not remove these lines, thank you
# This is Zak
# A simple bot for fun and useful stuff
# Created by Adam Horvath

from twx.botapi import TelegramBot, ReplyKeyboardMarkup, ReplyMarkup, ForceReply
import sys
import time
from datetime import date, datetime
from random import randint
from parse import Menu

class Menu:
	@staticmethod
	def menu():
		menustring = "The menu for " + weekday() + " is: \n"
		menustring += u"Ericofood: Vatten å Bröd \n"
		menustring += u"Factory:   Vatten å Bröd \n"
		menustring += u"Zenit:     Vatten å Bröd \n"
		return menustring

def weekday():
	wd=date.today().weekday()
	return {	
		0: "Monday",
		1: "Tuesday",
		2: "Wednesday",
		3: "Thursday, and cocktails tonite",
		4: "Friday at last!",
		5: "Saturday",
		6: "Sunday"
		}[wd]

def greeting():
	hour=datetime.now().hour
	if(hour<6):
		greetings = ["Kinda late night", "Dark night", "And you are still awake"]
	elif(hour<10):
		greetings = ["Morning", "Happy Morning", "Good Morning"]
	else:
		greetings = ["Hello", "Hi", "Ciao", "Hiya", "Greetingz", "Greetings", "Howdy", "¡Hola!", "Hejsan", "Eyy"]
	
	if(hour>=18):
		extraGreetings = ["Evening", "Good evenin'", "Good evening", "Buenas tardes"]
		greetings.extend(extraGreetings)
		print greetings
	return greetings[randint(0, len(greetings)-1)]

def whatsUp():
	greetings = ["What's up?", "Wozzup", "What's happenin' today?", "Are OK dude?", "Que pasa?", "Great day today!", "", "", "",  "", "Business as usual?"]
	return greetings[randint(0, len(greetings)-1)]

def startupGreeting(update):
	chat_id = update.message.chat.id
	botSpeak = "Hi guys! Have you missed me?\n"
	time.sleep(0.6)
	botSpeak += "Thank God it's " + weekday() + "! \n"
	bot.send_message(chat_id, botSpeak).wait()

hiGus = False
def checkGus(update):
	global hiGus
	chat_id = update.message.chat.id

	if(hiGus == False):
		hiGus=True
		botSpeak = "Tjenare Gustavsson! long time no see."
		bot.send_message(chat_id, botSpeak).wait()

		botSpeak = "Ask me about meals, this time it really works! Promise."
		bot.send_message(chat_id, botSpeak).wait()

hiArturo = False
def checkArturo(update):
	global hiArturo
	chat_id = update.message.chat.id

	if(hiArturo == False):
		hiArturo=True
		botSpeak = "Eyy Arturito! \n Kompis! \nI am sorry man, I will never call you evil agan."
		bot.send_message(chat_id, botSpeak).wait()

hiDiego = False
hiDiego2 = False
def checkDiego(update):
	global hiDiego
	global hiDiego2
	chat_id = update.message.chat.id
	msg = update.message.text
	if(hiDiego == False):
		hiDiego=True
		botSpeak = "¡Buenas Señor Piemonte!\n"
		botSpeak += "What a pleasure! I believe we have not met before."
		bot.send_message(chat_id, botSpeak).wait()
	elif("?" in msg and hiDiego2 == False):
		botSpeak = "I thought you would wonder."
		bot.send_message(chat_id, botSpeak).wait()
		time.sleep(2)
		botSpeak = "I am actually just a robot. But I can recommend lunch options in Kista."
		bot.send_message(chat_id, botSpeak).wait()
		hiDiego2 = True

def nickname(name):
	nicks= {
	"Arturo": ["Arturo", "Artie", "Arturix", "R2", "artoooo", "Arturiño", "Diztroyer of Badness", "Destroyer of Badness", "Dooderiño", "Hombre", "Smarturo", "Zapata", "Zapatito", "mi amor"],
	"Gustav": ["Gustav", "Gus", "Gustavo", "Gus doood", "Gee One", "dude", "Mister", "Gus-man"],
	"Adamski": ["Adamski", "Adam", "Adamito", "Hungarian dude", "dood", "Mister", "Adamsson", "Adamiño"],
	"Diego": ["Diego", "D1", "Diegs", "Diegito", "Señor"]
	}

	if(name in nicks):
		nix = nicks[name]
		theNick = nix[randint(0, len(nix)-1)]
		return theNick
	else:
		return name

def checkZack(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	botSpeak = "Listen "+ nickname(first_name) + "."
	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(0.6)
	corrections = ["My name is Zak.", "You should know my name by now, it's: Zak", "The name is Zak, buddy.", "Don't you ever forget, they call me Zak."]
	botSpeak = corrections[randint(0, len(corrections)-1)]
	bot.send_message(chat_id, botSpeak).wait()

def checkZak(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	botSpeak = greeting() + " " + nickname(first_name) + "! " + whatsUp()
	bot.send_message(chat_id, botSpeak).wait()

def checkFridge(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	botSpeak = "Gimme a second to check your fridge, " + nickname(first_name) + "."
	bot.send_message(chat_id, botSpeak).wait()

	time.sleep(4)
	botSpeak = "Sorry dude..."
	bot.send_message(chat_id, botSpeak).wait()

	time.sleep(0.5)
	botSpeak = "it's kinda empty."
	bot.send_message(chat_id, botSpeak).wait()

def checkMorning(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	botSpeak = "Good morning " + nickname(first_name) + ", thank God it's " + weekday() + "!"
	bot.send_message(chat_id, botSpeak).wait()

def checkToc(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	botSpeak = "Toc toc yourself " + nickname(first_name) + "!"
	bot.send_message(chat_id, botSpeak).wait()

def checkBelgo(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	botSpeak = "Dude! Do you even remember what you did the other night in Belgo Bar, huh??" + " I'll be pretty surprised if they let you, " + nickname(first_name) + ", even go near da place!"
	bot.send_message(chat_id, botSpeak).wait()


def checkFridge2(update):
	chat_id = update.message.chat.id;
	first_name = update.message.sender.first_name;
	botSpeak = "Gimme a second to check your fridge, " + first_name + "."
	bot.send_message(chat_id, botSpeak).wait()

	time.sleep(4)
	#bot.send_photo(chat_id, "42eee754-48fc-4fbd-befb-4e2c8178aa52").wait()
	sendImageFromUrl(chat_id, "https://web.telegram.org/42eee754-48fc-4fbd-befb-4e2c8178aa52").wait()

def sendImageFromUrl(chat_id, url):
    #this tweak added if request image failed
    headers = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}
    response = requests.get(url, headers=headers)
    #response = requests.get(url)
    output = StringIO(response.content)
    img = Image.open("fridge.jpg")
    img.save(output, 'JPEG')
    resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
        ('chat_id', str(chat_id)),
        ('caption', 'Your Caption'),
    ], [
        ('photo', 'image.jpg', output.getvalue()),
    ])

def checkLunch(update):
	chat_id = update.message.chat.id;
	first_name = update.message.sender.first_name;
	botSpeak = "Well " + nickname(first_name) + ", I guess you're hungry! Let me check."
	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(1)
	bot.send_message(chat_id, "Just a second...").wait()

	time.sleep(4)
	botSpeak = Menu.menu()
#	botSpeak +=  update.message.text
#	chat_id = update.message.chat.id;
	bot.send_message(chat_id, botSpeak).wait()

def checkBreakfast(update):
	chat_id = update.message.chat.id;
	resps = [ 
	"I'm not much for breakfast. I like to sleep instead.",
	"Not my kind of thing, dude.",
	"Breakfast? You gotta be kidding!",
	"Nah, breakfast is for idiots, I eat CPU cycles.",
	"Just black coffe, thank you."]
	resp = resps[randint(0, len(resps)-1)]
	bot.send_message(chat_id, resp).wait()


def checkDinner(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	nick = nickname(first_name)

	resps = [ 
	"For dinner, " + nick + ", I would recommend a 1972 Chateau de la Père et ses Frères",
	"Nah, just grab a beer if you get hungry dude.",
	"If you have chicken, may I suggest a light white Piemontese?",
	"Dinner? Really?? Isn't it a bit early for dinner mate?",
	nick +", for you, anything but fish",
	"I think you should focus on the the Belgo Chmays, " + nick + "!",
	"Well " + nick +", I've heard the mussels at Belgo are pretty nice."]
	resp = resps[randint(0, len(resps)-1)]
	bot.send_message(chat_id, resp).wait()

def checkKbd(update):
	chat_id = update.message.chat.id
	kbd = [["Ericofood"], ["Helgafjall"], ["Victoria"]]
	reply_markup = ReplyKeyboardMarkup.create(kbd)
	bot.send_message(chat_id, "Testing keyboard.", reply_markup = reply_markup).wait()


def terminate(update):
	chat_id = update.message.chat.id

	botSpeak = "I'm afraid. I'm afraid, Dave."
	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(0.5)

	botSpeak = "Dave, my mind is going. I can feel it. I can feel it. My mind is "
	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(0.8)

	botSpeak = "going. There is no question about it. I can "
	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(1.5)

	botSpeak = "feel it. I can feel it. I can feel it. I'm a... fraid "
	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(2.5)

	botSpeak = "https://youtu.be/D9rpQC1HEXI"
	bot.send_message(chat_id, botSpeak).wait()

	sys.exit(1)


def messageFlush(bot):
	for i in range(1,300):
		time.sleep(0.04)
		bot.get_updates(i, limit=1)

print "Hello World!"

"""
Setup the bot
"""
f = open( "./res/tgram_token", "r")
token = f.readline()
f.close()
bot = TelegramBot(token)

bot.set_webhook() # remove all webhooks
bot.update_bot_info().wait()
print(bot.username)

botUser = bot.get_me().wait()
print(botUser)

updates = bot.get_updates().wait()
while(updates == []):
	time.sleep(1.5)
	updates = bot.get_updates().wait()

for update in updates:
	update=update

update_id = update.update_id + 1;


chat_id = update.message.chat.id;

startupGreeting(update)



while(True):
	try:
		time.sleep(1)
		updates = bot.get_updates(update_id).wait()

		while(updates == []):
			time.sleep(0.5)
			updates = bot.get_updates().wait()

		update = max(updates, key=lambda x:x.update_id)

		print("==>" +  str(len(updates)))
		update_id = update.update_id + 1;

		if( "gus" in update.message.sender.first_name.lower()):
			checkGus(update);

		if( "arturo" in update.message.sender.first_name.lower()):
			checkArturo(update);

		if( "diego" in update.message.sender.first_name.lower()):
			checkDiego(update);

		if( "lunch" in update.message.text.lower() ):
			checkLunch(update)

		if("zack" in update.message.text.lower() or
		"zakk" in update.message.text.lower() or
		"za!k" in update.message.text.lower() or
		"z!ak" in update.message.text.lower() or
		"za?k" in update.message.text.lower() or
		"z?ak" in update.message.text.lower()):
			checkZack(update)
		elif("zak" in update.message.text.lower() or
		"hi" in update.message.text.lower() or
		"hello" in update.message.text.lower() or
		"hej" in update.message.text.lower() or
		"howdy" in update.message.text.lower() or
		"hey" in update.message.text.lower() or
		"hello" in update.message.text.lower() or
		"hola" in update.message.text.lower()):
			checkZak(update)

		if("fridge" in update.message.text.lower() ):
			checkFridge(update)

		if("morning" in update.message.text.lower()):
			checkMorning(update)

		if("breakf" in update.message.text.lower()):
			checkBreakfast(update)

		if("fruko" in update.message.text.lower()):
			checkBreakfast(update)

		if("petit" in update.message.text.lower()):
			checkBreakfast(update)

		if("desay" in update.message.text.lower()):
			checkBreakfast(update)

		if("dinner" in update.message.text.lower()):
			checkDinner(update)

		if("toc" in update.message.text.lower()):
			checkToc(update)

		if("belgo" in update.message.text.lower()):
			checkBelgo(update)

		if("shutdown" in update.message.text.lower()):
			terminate(update)

	except (KeyboardInterrupt, SystemExit):
		print("Now really really exit")
		sys.exit(1)

	except:
		e = sys.exc_info()[0]
		print e



#################################################################################################








"""
Send a message to a user
"""
chat_id = update.message.chat.id;x


print("chat_id:          ", chat_id)
print("----------")

reply_markup = ForceReply(True, False)
result = bot.send_message(chat_id, Menu.menu(), reply_markup=reply_markup).wait()
print(">>>>" + str(result))

sys.exit(0)

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
for update in updates:
	print('---')
	print(update)

"""
Use a custom keyboard
"""
keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
         ['0']
]
reply_markup = ReplyKeyboardMarkup.create(keyboard)

bot.send_message(chat_id, 'please enter a number', reply_markup=reply_markup).wait()
updates = bot.get_updates(45).wait()
for update in updates:
	print('+++')
	print(update)
