import logging
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import Sticker
from telegram import StickerSet
from telegram.ext import Updater
from telegram.ext import CommandHandler
import random
import json


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

file = open('sets_lists/mops_dyadya_pyos.json', 'r')
stickers_list = json.load(file)
file.close()


def start(update, context):
    btn = [[KeyboardButton('/help')]]
    msg = 'Привет! Нажми на кнопку, чтобы узнать как я работую'
    markup = ReplyKeyboardMarkup(btn, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(msg, reply_markup=markup)


def alarm(context):
    job = context.job
    context.bot.send_sticker(job.context, random.choice(stickers_list))


def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text("Время меньше нуля")
            return

        if 'timer' in context.chat_data:
            old_timer = context.chat_data['timer']
            old_timer.schedule_removal()

        new_timer = context.job_queue.run_once(alarm, due, context=chat_id)
        context.chat_data['timer'] = new_timer

        update.message.reply_text("Таймер был установлен!!!")

    except(IndexError, ValueError):
        update.message.reply_text("Использовается так: /set <seconds>")


def unset(update, context):
    if "timer" not in context.chat_data:
        update.message.reply_text("У вас нет активного таймера")
        return
    timer = context.chat_data['timer']
    timer.schedule_removal()
    del context.chat_data['timer']
    update.message.reply_text("Таймер удален")


def help(update, context):
    update.message.reply_text(text="Используй /set <seconds> чтобы утановить таймер.\n"
                                   "/unset отключит сущесвующий таймер. \n")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("set", set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
