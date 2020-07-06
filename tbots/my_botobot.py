import telebot

token = '-'
bot = telebot.TeleBot(token)
import random
import re

greet = ["Привет!", "Здравствуй!", "Здравствуйте!", "Приветствую!"]
ans1 = ["Норм", "Все хорошо", "Все нормально"]
ans2 = ["Я бот который отвечает на твои вопросы =)", "Сижу и отвечаю на твои вопросы", "Переписываюсь с тобой, конечно"]


@bot.message_handler(content_types=['text'])
def ans(message):
    if re.search("(привет|здравствуй|приветствую|день добрый)", message.text.lower()):
        bot.send_message(message.chat.id, random.choice(greet))
    elif re.match("^(.)*(как)(.)*(дела|поживаешь|делишки)(.)*(\?)+(.)*", message.text.lower()):
        bot.send_message(message.chat.id, random.choice(ans1))
        bot.send_message(message.chat.id, "А как у тебя дела?")
    elif re.match("^(.)*(норм|нормально|не плохо)[а-яА-Я\s]*", message.text.lower()):
        bot.send_message(message.chat.id, "Я рад!")
    elif re.match("^(.)*(хорошо|отлично|супер)[а-яА-Я\s]*", message.text.lower()):
        bot.send_message(message.chat.id, "Здорово!!")
    elif re.match("^(.)*(плохо|так себе|не очень)(.)*", message.text.lower()):
        bot.send_message(message.chat.id, "Что случилось?")
    elif re.match("^(.)*(чем|что)[а-яА-Я\s]*(делаешь|занимаешься)[а-яА-Я\s]*(\?)+(.)*", message.text.lower()):
        bot.send_message(message.chat.id, random.choice(ans2))
    else:
        bot.send_message(message.chat.id, "Я не понял что ты сказал, извини :(")


bot.infinity_polling()