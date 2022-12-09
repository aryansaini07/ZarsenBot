from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from datetime import datetime
import chatbot
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_time = str(current_time)
updater = Updater("5577863946:AAEwl39xVTP0xRpY-HQBTEuT0yw1NtqwH6o",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello, Welcome to the Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/time - To get the current time
	/linkedin - To get the LinkedIn profile URL
	/gmail - To get gmail URL
	/about - To Knownabout developer
    """)


def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Your gmail link here aryansaini0702@gmail.com")


def time_url(update: Update, context: CallbackContext):
	update.message.reply_text("Cuttent Time is \
	"+ current_time)


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"LinkedIn URL => \
		https://www.linkedin.com/in/aryan-saini-566605212/")


def about_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"About Developer => This telegram chatbot is developed by Aryan Saini and Shubham Sharma, This ia basic Chatbot for testing purpose.")


def unknown(update: Update, context: CallbackContext):
    msg = update.message.text
    reply = chatbot.chat(msg)
    update.message.reply_text(str(reply))




updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('time', time_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('about', about_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.


updater.start_polling()
