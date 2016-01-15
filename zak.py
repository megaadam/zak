# -*- coding: utf-8 -*-
# Please do not remove these lines, thank you
# This is Zak
# A simple bot for fun and useful stuff
# Created by Adam Horvath

from twx.botapi import TelegramBot, ReplyKeyboardMarkup, ReplyMarkup, ForceReply
import sys, traceback
import time
from random import randint, shuffle
import re


from parse import Menu
from phrases import Phrase
from util import T, Msg

def greeting():
	if(T.hour()<6):
		greetings = ["Kinda late night", "Dark night", "And you are still awake"]
	elif(T.hour()<10):
		greetings = ["Morning", "Happy Morning", "Good Morning"]
	else:
		greetings = ["Hello", "Hi", "Ciao", "Hiya", "Greetingz", "Greetings", "Howdy", "¡Hola!", "Hejsan", "Eyy"]
	
	if(T.hour()>=18):
		extraGreetings = ["Evening", "Good evenin'", "Good evening", "Buenas tardes"]
		greetings.extend(extraGreetings)
		print greetings
	return greetings[randint(0, len(greetings)-1)]

def whatsUp():
	greetings = ["What's up?", "Wozzup", "What's happenin' today?", "Are OK dude?", "¿Que pasa?", "Great day today!", "", "", "",  "", "Business as usual?"]
	return greetings[randint(0, len(greetings)-1)]

def startupGreeting(msg):
	botSpeak = vocab.getGreeting1(msg)
	bot.send_message(chat_id, botSpeak).wait()

	time.sleep(1.5)
	botSpeak = vocab.getGreeting2(msg)
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

hiStefano = False
def checkStefano(msg):
	global hiStefano

	if(hiStefano == False):
		hiStefano=True
		botSpeak = vocab.getHiStefano(msg)
		bot.send_message(msg.chatId, botSpeak).wait()

hiArturo = False
def checkArturo(msg):
	global hiArturo

	if(hiArturo == False):
		hiArturo=True
		botSpeak = vocab.getHiArturo(msg)
		bot.send_message(msg.chatId, botSpeak).wait()

hiNewYear = False
def checkNewYear():
	global hiNewYear
	if(hiNewYear == False and T.year() == 2016 and T.month() == 1 and T.day() == 1 and T.hour() == 0 and T.minute() == 0):
		bot.send_message(msg.chatId, "Hey you awesome dudes").wait()
		bot.send_message(msg.chatId, "I just want to say...").wait()
		time.sleep(1.1)
		bot.send_message(msg.chatId, "*H*A*P*PY* *N*E*W* *Y*E*A*R*").wait()
		hiNewYear = True



hiDiego2 = False
def checkDiego(update):
	global hiDiego
	global hiDiego2
	chat_id = update.message.chat.id
	msg = update.message.text
	if(hiDiego == False):
		hiDiego=True
		botSpeak = "¡Buenas Señor Piemonte!\n"
		botSpeak += "What a pleasure!"
		bot.send_message(chat_id, botSpeak).wait()
	elif("?" in msg and hiDiego2 == False):
		botSpeak = "I thought you would wonder."
		bot.send_message(chat_id, botSpeak).wait()
		time.sleep(2)
		botSpeak = "I am actually just a robot. But I can recommend lunch options in Kista."
		bot.send_message(chat_id, botSpeak).wait()
		hiDiego2 = True

def checkBeardless(msg):
	botSpeak = vocab.getBeardless(msg)
	bot.send_message(chat_id, botSpeak).wait()

def checkSwedish(update):
	chat_id = update.message.chat.id
	msg = update.message.text
	nick = nickname(update.message.sender.first_name)
	botSpeak = vocab.swedish(nick)
	bot.send_message(chat_id, botSpeak).wait()


def checkGithub(update):
	chat_id = update.message.chat.id
	msg = update.message.text
	nick = nickname(update.message.sender.first_name)
	if("?" in msg):
		botSpeak = "Good question " + nick + "!"
		bot.send_message(chat_id, botSpeak).wait()
		time.sleep(2.2)
	else:
		botSpeak = "Well " + nick + ","
		bot.send_message(chat_id, botSpeak).wait()
		time.sleep(0.2)
	botSpeak = "My source code is in Python \nYou can in fact expect to find it at https://github.com/megaadam/zak" 
	bot.send_message(chat_id, botSpeak).wait()


def nickname(name):
	return vocab.nickname(name)

def checkZack(update):
	chat_id = update.message.chat.id;
	nick = nickname(update.message.sender.first_name)
	botSpeak = vocab.getZack1(nick)

	bot.send_message(chat_id, botSpeak).wait()
	time.sleep(0.6)
	botSpeak = vocab.getZack2(nick)
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
	botSpeak = "Good morning " + nickname(first_name) + ", thank God it's " + T.weekday() + "!"
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

def genericLunch(msg):
	name = msg.sender
	nick = nickname(name)
	botSpeak = "Well " + nick + ", I guess you're hungry! Let me check."
	bot.send_message(msg.chatId, botSpeak).wait()

	if(theMenu.getLocalMode() == True):
		botSpeak = "[Sorry, offline mode :( demo menus from December 10]\n"
	else:
		botSpeak =""

	rest = vocab.rnd(theMenu.getRestaurants())
	food = vocab.rnd(theMenu.getFoods(rest))

	botSpeak += "Today I would avoid " + rest + " and their tasteless " + food + "."
	print botSpeak
	bot.send_message(msg.chatId, botSpeak).wait()

	rest = vocab.rnd(theMenu.getRestaurants())
	food = vocab.rnd(theMenu.getFoods(rest))
	botSpeak = "But you could try the interesting " + food + " at " + rest + "."
	print botSpeak
	bot.send_message(msg.chatId, botSpeak).wait()

def checkFood(msg):
	nick = nickname(msg.sender)

	if(T.hour() < 6):
		botSpeak = vocab.getMidnightFood(msg)
		bot.send_message(msg.chatId, botSpeak).wait()
		return

	if(msg.sender == "arturo"):
		botSpeak = vocab.getArtFood(msg)
		bot.send_message(msg.chatId, botSpeak).wait()
		return

	botSpeak = vocab.getFood(msg)
	bot.send_message(msg.chatId, botSpeak).wait()

def checkLunch(msg):
	nick = nickname(msg.sender)

	if(T.hour() < 6):
		botSpeak = nick + "! Don't be ridiculous. This is not the time for lunch, and you should be asleep."
		bot.send_message(msg.chatId, botSpeak).wait()
		return

	if(T.weekend()):
		botSpeak = nick + " get real! The Kista restaurants are closed on " + T.weekday() + "s"
		bot.send_message(msg.chatId, botSpeak).wait()
		return

	if(T.hour() < 10):
		botSpeak = "I think it's a bit early for lunch. Ask me after 10 again."
		bot.send_message(msg.chatId, botSpeak).wait()
		return

	if(T.hour() < 14):
		genericLunch(msg)
		return

	if(T.hour() < 18):
		botSpeak = "No such thing as a free lunch " + nick + ". Too late anyway."
		bot.send_message(msg.chatId, botSpeak).wait()
		return

	botSpeak = "At this hour, " + nick + "... I would rather recommend dinner."
	bot.send_message(msg.chatId, botSpeak).wait()

def checkRestaurants(update):
	chat_id = update.message.chat.id;
	nick = nickname(update.message.sender.first_name)
	r = theMenu.getRestaurants()
	shuffle(r)
	botSpeak = vocab.restaurants(nick, r)
	bot.send_message(chat_id, botSpeak).wait()

def checkBreakfast(update):
	chat_id = update.message.chat.id;
	nick = nickname(update.message.sender.first_name)
	botSpeak = vocab.breakfast(nick)
	bot.send_message(chat_id, botSpeak).wait()

def checkGlaze(update):
	chat_id = update.message.chat.id;
	nick = nickname(update.message.sender.first_name)
	botSpeak = vocab.getGlaze(nick)
	bot.send_message(chat_id, botSpeak).wait()

def checkDinner(update):
	chat_id = update.message.chat.id
	first_name = update.message.sender.first_name
	nick = nickname(first_name)
	bot.send_message(chat_id, vocab.dinner(nick)).wait()

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



theMenu = Menu()
vocab = Phrase()

chat_id = update.message.chat.id
msgTxt = update.message.text.lower()
msgTokens = msgTxt.split(u'\s,;.:!?¡¿+-*/="\'\\')
msgSender = update.message.sender.first_name.lower()
msg = Msg(chat_id, msgTxt, msgTokens, msgSender)
startupGreeting(msg)


while(True):
	try:
		time.sleep(1.1)
		updates = bot.get_updates(update_id).wait()

		while(updates == []):
			checkNewYear()
			time.sleep(1.1)
			updates = bot.get_updates().wait()

		update = max(updates, key=lambda x:x.update_id)
		update_id = update.update_id + 1;

		chat_id = update.message.chat.id
		msgTxt = update.message.text.lower()
		msgTokens = re.split(',|;|!|\?|\.|\+|-|\*|/|=|¿|\s', msgTxt)
		msgSender = update.message.sender.first_name.lower()
		# msgSender = "arturo"

		msg = Msg(chat_id, msgTxt, msgTokens, msgSender)

		# special first
		if("restaurang" in msgTxt or
		u"å" in msgTxt or	
		u"ä" in msgTxt or	
		u"ö" in msgTxt or	
		"fruko" in msgTxt or	
		"jatte" in msgTxt or	
		"tack" in msgTxt or	
		"hej" in msgTokens	or
		"bra" in msgTokens):
			checkSwedish(update)

		# dudes
		if( "gus" in msgSender):
			checkGus(update)

		if( "arturo" in msg.sender):
			checkArturo(msg)

		if( "diego" in msgSender):
			checkDiego(update)

		if( "stefano" in msgSender):
			msg.sender = "stefano"
			checkStefano(msg)

		# Greetings
		if("zack" in msgTxt or
		"zakk" in msgTxt or
		"zakie" in msgTxt or
		"zok" in msgTxt or
		"za!k" in msgTxt or
		"z!ak" in msgTxt or
		"za?k" in msgTxt or
		"z?ak" in msgTxt):
			checkZack(update)
		elif("zak" in msgTokens or
		"hi" in msgTokens or
		"hello" in msgTokens or
		"hej" in msgTokens or
		"howdy" in msgTokens or
		"hey" in msgTokens or
		"hello" in msgTokens or
		"hola" in msgTokens):
			checkZak(update)


		# fragments
		if( "lunch" in msgTxt ):
			checkLunch(msg)

		if( "food" in msgTxt ):
			checkFood(msg)

		if("resta" in msgTxt):
			checkRestaurants(update)

		if("fridge" in msgTxt ):
			checkFridge(update)

		if("breakf" in msgTxt):
			checkBreakfast(update)

		if("fruko" in msgTxt):
			checkBreakfast(update)

		if("petit" in msgTxt):
			checkBreakfast(update)

		if("desay" in msgTxt):
			checkBreakfast(update)
		if("morning" in msgTokens):
			checkMorning(update)

		if("belgo" in msgTxt):
			checkBelgo(update)

		if("github" in msgTxt or
		"source" in msgTxt or
		"python" in msgTxt):
			checkGithub(update)

		# words
		if("glaze" in msgTokens):
			checkGlaze(update)

		if("dinner" in msgTokens):
			checkDinner(update)

		if("toc" in msgTokens):
			checkToc(update)

		if("beardless" in msgTokens and "?" in msgTxt):
			checkBeardless(msg)

		if("shutdown" in msgTokens):
			terminate(update)

	except (KeyboardInterrupt, SystemExit):
		print("Now really really exit")
		sys.exit(1)

	except:
		traceback.print_exc()



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
