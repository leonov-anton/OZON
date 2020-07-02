import logging
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

button_help = '/help'

def start(update, context):
    keybord = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=button_help)]])
    update.message.reply_text(text="Привет! Используй /set <seconds> чтобы утановить таймер или нажми на кнопку снизу",
                              reply_makrup=keybord)

def alarm(context):
    job = context.job
    context.bot.send_message(job.context, text="Бип-Бип")


def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text("Время меньше нуля")
            return

        if 'timer' in context.chat_data:
            old_timer = context.chat_data['timer']
            old_timer.shedule_removal()

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
    timer.shedule_removal()
    del context.chat_data['timer']
    update.message.reply_text("Таймер удален")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_error_handler(error)

    updater.start_polling()

main()