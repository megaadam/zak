# -*- coding: utf-8 -*-

from twx.botapi import TelegramBot, ReplyKeyboardMarkup, ReplyMarkup, ForceReply
import sys
import time


class Menu:
	@staticmethod
	def menu():
		menustring = "The menu for " + Menu.weekday() + " is: \n"
		menustring += u"Ericofood: Surströmming \n"
		menustring += u"Factory:   Surströmming \n"
		menustring += u"Zenit:     Surströmming \n"

		return menustring

	@staticmethod
	def weekday():
		return "Friday"

def checkLunch(update):
	first_name = update.message.sender.first_name;
	botSpeak = "Hello " + first_name + ", I guess you're hungry! Let me check."
	bot.send_message(chat_id, botSpeak).wait()
	bot.send_message(chat_id, "Just a second...").wait()

	time.sleep(1)

	botSpeak = Menu.menu()
#	botSpeak +=  update.message.text
#	chat_id = update.message.chat.id;
	bot.send_message(chat_id, botSpeak).wait()

def messageFlush(bot):
	for i in range(1,300):
		time.sleep(0.04)
		bot.get_updates(i, limit=1)

print "Hello World!"

"""
Setup the bot
"""

bot = TelegramBot('172048491:AAG253i7GAR-AxQTX7bZlhlJmAPQu6n_3b0')
bot.set_webhook() # remove webhook
bot.update_bot_info().wait()
print(bot.username)

botUser = bot.get_me().wait()
print(botUser)

#updates = bot.get_updates(159).wait()
#for update in updates:
#	update=update

#print("update:           ", update)

#message_id = update.message.message_id;
#first_name = update.message.sender.first_name;


#print( "message_id: ", message_id)
#print( "name: ", first_name)

reply_markup = ForceReply(True, False)

#messageFlush(bot)

updates = bot.get_updates().wait()
while(updates == []):
	time.sleep(0.5)
	updates = bot.get_updates().wait()


for update in updates:
	update=update

print(update)
update_id = update.update_id + 1;
print(update_id)
print("-------------------------------------------")
chat_id = update.message.chat.id;
#bot.send_message(chat_id, "Hi Arturo. How are you feeling today?").wait()
#bot.send_message(chat_id, "Well Buddy... you could imagine. I am stuck in Adam's laptop. You're out there breathing fresh air, and chcking out the girls.").wait()
bot.send_message(chat_id, "These Spanish dudez you know...").wait()



while(True):
	time.sleep(1)
	updates = bot.get_updates(update_id).wait()
	while(updates == []):
		time.sleep(0.5)
		updates = bot.get_updates().wait()
		for update in updates:
			update=update
	print("==========")		
	print(update_id)
	tmp_update_id = update.update_id;
	if(True): 
		update_id = update.update_id + 1;
		print(update_id)

		if( "lunch" in update.message.text.lower() ):
			checkLunch(update)



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
