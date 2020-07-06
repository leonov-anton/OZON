import telebot
import json

token = '-'
bot = telebot.TeleBot(token)
a = []


@bot.message_handler(content_types=['sticker', 'text'])
def get_msg(message):
    print(message)


bot.infinity_polling()
