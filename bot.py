from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler, Filters

import telebot
from telebot import types

import telebot

bot = telebot.TeleBot("1419594629:AAHrp5k1zvPFndBxjswXkqBE4e0fjY96GD8")


@bot.message_handler(content_types=['new_chat_members'])
def delete_join_message(m):
    # If bot is not admin, then it will not be able to delete message.
    try:
        bot.delete_message(m.chat.id,m.message_id)
    except:
        if m.new_chat_member.id != bot.get_me().id:
            bot.send_message(m.chat.id,"Please make me an admin in order for me to remove the join and leave messages on this group!")
        else:
            bot.send_message(m.chat.id,"Hi! I am your trusty GroupSilencer Bot! Thanks for adding me! To use me, make me an admin and I will be able to delete all the pesky notification when a member joins or leaves the group!")

@bot.message_handler(content_types=['left_chat_member'])
def delete_leave_message(m):
    # If bot is the one that is being removed, it will not be able to delete the leave message.
    if m.left_chat_member.id != bot.get_me().id:
        try:
            bot.delete_message(m.chat.id,m.message_id)
        except:
            bot.send_message(m.chat.id,"Please make me an admin in order for me to remove the join and leave messages on this group!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "😋 Please add me to your groups\n    እባክዎን ወደ ቡድኖችዎ  ያስገቡኝ  \n            👇👇\n  https://t.me/JoinHiderGTIBot?startgroup=inpvbtn \n\n ❗️ Do not forget that in order to be able to do my job properly, I must be the group administrator and have the necessary permissions.\n ❗️ ሥራዬን በአግባቡ ለመወጣት የቡድን አስተዳዳሪ መሆን እና አስፈላጊ ፈቃዶች መኖሬን መዘንጋት የለብዎትም።")  \





bot.polling()
