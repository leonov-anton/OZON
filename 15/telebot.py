# -*- coding: utf-8 -*-
"""Telebot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JXVJrFOM3BYf7in7RklmseYvKwJo99UF
"""

# pip install pyTelegramBotAPI

import telebot
token = '1201754694:AAEi7a-0vSHWAyUKI4isbo-kJHsxriErF7Y'
bot = telebot.TeleBot(token)
import random
devizions = ["Ozon the best", "Люблю Ozon"]

@bot.message_handler(content_types=['text'])
def acho(message):
  if message.text.lower() == "ozon":
    bot.send_message(message.chat.id, random.choice(devizions))

bot.infinity_polling()

# pip install python-telegram-bot
#
# pip install -U ipykernel

import logging
import telegram.ext.Updater
import telegram.ext.CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
  update.message.reply_text("Привет! Используй /set <seconds> чтобы утановить таймер")
  
def alarm(context):
  job = context.job
  context.bot.send_message(job.context, text='Бип')

def set_timer(update, context):
  chat_id = updete.message.chat_id
  try:
    due = int(context.args[0])
    if due < 0:
      update.message.reply_text("Время меньше нуля")
      return
    if "job" in context.chat_data:
      old_job = context.chat_data['job']
      old_job.schedule_removal()
    new_job = context.job_queue.rum_once(alarm, due, context=chat_id)
    context.chat_data['job'] = new_job
    update.message.reply_text("Таймер был установлен!!!")
  except(IndexError, ValueError):
    update.message.reply_text("Использовается так: /set <seconds>")

def unset(update, context):
  if "job" not in context.chat_data:
    update.message.reply_text("У вас нет активного таймера")
    return
  job = cpntext.chat_data['job']
  job.schedule_removal()
  del context.chat_data['job']

  update.message.reply_text("Таймер удален")

def error(update, context):

  logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
  updater = updater('1201754694:AAEi7a-0vSHWAyUKI4isbo-kJHsxriErF7Y', use_context=True)
  dp = updater.dispatcher

  dp.add_handler(CommandHandler("start", start))
  dp.add_handler(CommandHandler("help", start))
  dp.add_handler(CommandHandler("set", set_timer, pass_args=True,
                                pass_job_queue=True, pass_chat_data=True))
  dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
  dp.add_error_handler(error)
  update.start_polling()

main()