# - *- coding: utf- 8 - *-

import logging
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import ShippingQueryHandler
import re
import time
import datetime
from datetime import datetime, timedelta, timezone
from dateutil import tz


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

users_id = []


def start(update, context):
    btn = [[KeyboardButton('/help'), KeyboardButton('/todo_list')]]
    msg = 'Привет! Я бот который поможет не забыть о твоих планах. ⏰ \n\n' \
          'Используй /set <текст заметки и время в формате ЧЧ:ММ> чтобы добавить напоминание.\n' \
          'Я пришлю тебе сообщение в указанное время сегодня.🔖\n' \
          'Используй /todo_list чтобы просматривать и управлять своими напоминаниями. 📝\n\n' \
          'Если не хочется писать, можно нажать на кнопки ниже.\n\n' \
          'Используй /help если захочешь прочитать это сообщение снова.'
    markup = ReplyKeyboardMarkup(btn, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(msg, reply_markup=markup)
    if update.message.chat_id not in users_id:
        users_id.append(update.message.chat_id)


def alarm(context):
    job = context.job
    context.bot.send_message(job.context, job.name)


def set_timer(update, context):

    task_time = ''
    task_date = ''

    for i in context.args:
        if re.search(r'(\d\d)(:)(\d\d)', i):
            task_time = i
        elif re.search(r'(\d\d)(\.)(\d\d)', i) or re.search(r'(\d\d)(\.)(\d\d)(\.)(\d\d\d\d)', i):
            task_date = i

    if task_time == True and task_date == False and re.search(r'(З|завтра)', update.message.text[5:]) == False:
        task_time = task_time.split(':')
        time_now = datetime.now()
        utc = tz.tzutc()
        due = datetime(time_now.year, time_now.month, time_now.day, int(task_time[0]),
                       int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id, name=update.message.text[5:])
        context.chat_data[str(update.message.text[5:])] = new_timer
        update.message.reply_text("Запись внесена в список дел.")

    elif task_time and task_date:
        task_time = task_time.split(':')
        task_date = task_date.split('.')
        time_now = datetime.now()
        utc = tz.tzutc()
        if len(task_date) == 3:
            due = datetime(int(task_date[2]), int(task_date[1]), int(task_date[0]), int(task_time[0]),
                        int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id, name=update.message.text[5:])
        else:
            due = datetime(time_now.year, int(task_date[1]), int(task_date[0]), int(task_time[0]),
                           int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                   name=update.message.text[5:])
        context.chat_data[str(update.message.text[5:])] = new_timer
        update.message.reply_text("Запись внесена в список дел.")

    elif re.search(r'(З|завтра)', update.message.text[5:]) and task_time:
        task_time = task_time.split(':')
        time_now = datetime.now()
        utc = tz.tzutc()
        try:
            due = datetime(time_now.year, time_now.month, time_now.day + 1, int(task_time[0]),
                        int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                name=update.message.text[5:])
        except:
            due = datetime(time_now.year, time_now.month + 1, 1, int(task_time[0]),
                           int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                   name=update.message.text[5:])
        context.chat_data[str(update.message.text[5:])] = new_timer
        update.message.reply_text("Запись внесена в список дел.")

    else:
        update.message.reply_text("Не указано время. Надо писать время в формате ЧЧ:ММ.")



def unset(update, context):
    try:
        number = int(context.args[0]) - 1
        todo_list = [i for i in context.chat_data]
        timer = context.chat_data[todo_list[number]]
        timer.schedule_removal()
        del context.chat_data[todo_list[number]]
        update.message.reply_text("Задача удалена.")
    except(IndexError, ValueError):
        update.message.reply_text("Нужно писать: /unset <номер в списке>")


def todo_list_view(update, context):

    time_now = datetime.now()
    # todo_list = context.chat_data
    last_tasks = []
    todo_list_msg = ''
    number = 1

    if context.chat_data:
        for i in context.chat_data:
            todo_time = re.search(r'(\d\d)(:)(\d\d)', i)
            todo_time = todo_time.group(0)
            todo_time = todo_time.split(':')

            if int(todo_time[0]) > time_now.hour:
                number_str = f'{number}. '
                todo_list_msg += number_str + i.capitalize()
                todo_list_msg += '\n'
                number += 1

            elif int(todo_time[0]) == time_now.hour and int(todo_time[1]) > time_now.minute:
                number_str = f'{number}. '
                todo_list_msg += number_str + i.capitalize()
                todo_list_msg += '\n'
                number += 1

            else:
                last_tasks.append(i)

        if todo_list_msg:
            update.message.reply_text(text=f'{todo_list_msg}\n'
                                        '🗑 Чтобы удалить задачу напиши /unset <номер в списке>.')
        else:
            update.message.reply_text(text='У тебя нет задач.')
    else:
        update.message.reply_text(text='У тебя нет задач.')

    for i in last_tasks:
        del context.chat_data[i]


def broadcast_message(update, context):
    if update.message.chat_id == 195177538:
        message_text = update.message.text[11:]
        for i in users_id:
            context.bot.send_message(i, message_text)


def save_users_list(update, context):
    print(users_id)
    pass


def help():
    pass


def msg_set(update, context):

    text = update.message.text.split(' ')

    task_time = ''
    task_date = ''

    for i in text:
        if re.search(r'(\d\d)(:)(\d\d)', i):
            task_time = i
        elif re.search(r'(\d\d)(\.)(\d\d)', i) or re.search(r'(\d\d)(\.)(\d\d)(\.)(\d\d\d\d)', i):
            task_date = i

    if task_time and re.search(r'(З|завтра)', update.message.text) == False:
        task_time = task_time.split(':')
        time_now = datetime.now()
        utc = tz.tzutc()
        due = datetime(time_now.year, time_now.month, time_now.day, int(task_time[0]),
                       int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id, name=update.message.text)
        context.chat_data[str(update.message.text)] = new_timer
        update.message.reply_text("Запись внесена в список дел.")

    elif task_time and task_date:
        task_time = task_time.split(':')
        task_date = task_date.split('.')
        time_now = datetime.now()
        utc = tz.tzutc()
        if len(task_date) == 3:
            due = datetime(int(task_date[2]), int(task_date[1]), int(task_date[0]), int(task_time[0]),
                        int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id, name=update.message.text[5:])
        else:
            due = datetime(time_now.year, int(task_date[1]), int(task_date[0]), int(task_time[0]),
                           int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                   name=update.message.text[5:])
        context.chat_data[str(update.message.text)] = new_timer
        update.message.reply_text("Запись внесена в список дел.")

    elif re.search(r'(З|завтра)', update.message.text) and task_time:
        task_time = task_time.split(':')
        time_now = datetime.now()
        utc = tz.tzutc()
        try:
            due = datetime(time_now.year, time_now.month, time_now.day + 1, int(task_time[0]),
                        int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                name=update.message.text)
        except:
            due = datetime(time_now.year, time_now.month + 1, 1, int(task_time[0]),
                           int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                   name=update.message.text)
        context.chat_data[update.message.text] = new_timer
        update.message.reply_text("Запись внесена в список дел.")

    else:
        update.message.reply_text("Не указано время. Надо писать время в формате ЧЧ:ММ.")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(MessageHandler(Filters.regex('(\d\d)(:)(\d\d)'), msg_set, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("set", set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_handler(CommandHandler("todo_list", todo_list_view, pass_chat_data=True))
    dp.add_handler(CommandHandler("1984_admin", broadcast_message))
    dp.add_handler(CommandHandler("1984_admin_save", save_users_list))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
