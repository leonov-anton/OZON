# - *- coding: utf- 8 - *-

import logging
import re
import datetime
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from datetime import datetime, timedelta, timezone
from dateutil import tz
import pytz
from timezonefinder import TimezoneFinder

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# global variables
users_id = []
utc = tz.tzutc()



def start(update, context):
    btn = [[KeyboardButton('/help'), KeyboardButton('/todo_list')]]
    msg = 'Привет! Я бот который поможет не забыть о твоих планах. ⏰ \n\n' \
          'Напиши сообщение которое содержит время в формате ЧЧ:ММ чтобы добавить напоминание на сегодня.\n' \
          'Или укажи дату в формета ДД.ММ.ГГ или напиши в сообщении "завтра" так же указав время. \n' \
          'Я пришлю тебе сообщение в указанное время.🔖\n' \
          'Написав /todo_list можно просматривать и управлять своими напоминаниями. 📝\n' \
          'Напиши /help если захочешь прочитать это сообщение снова.\n\n' \
          'Если не хочется писать, можно нажать на кнопки ниже.'
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
        due = datetime(time_now.year, time_now.month, time_now.day, int(task_time[0]),
                       int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id, name=update.message.text[5:])
        context.chat_data[str(update.message.text[5:])] = new_timer
        update.message.reply_text("Запись внесена в список дел")

    elif task_time and task_date:
        task_time = task_time.split(':')
        task_date = task_date.split('.')
        time_now = datetime.now()
        if len(task_date) == 3:
            due = datetime(int(task_date[2]), int(task_date[1]), int(task_date[0]), int(task_time[0]),
                           int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                   name=update.message.text[5:])
        else:
            due = datetime(time_now.year, int(task_date[1]), int(task_date[0]), int(task_time[0]),
                           int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
            new_timer = context.job_queue.run_once(alarm, due, context=update.message.chat_id,
                                                   name=update.message.text[5:])
        context.chat_data[str(update.message.text[5:])] = new_timer
        update.message.reply_text("Запись внесена в список дел")

    elif re.search(r'(З|завтра)', update.message.text[5:]) and task_time:
        task_time = task_time.split(':')
        time_now = datetime.now()
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
        update.message.reply_text("Запись внесена в список дел")

    else:
        update.message.reply_text("Не указано время. Необходимо писать время в формате ЧЧ:ММ")


def unset(update, context):
    try:
        number = int(context.args[0]) - 1
        todo_list = [i for i in context.chat_data]
        timer = context.chat_data[todo_list[number]]['job']
        timer.schedule_removal()
        del context.chat_data[todo_list[number]]
        update.message.reply_text("Задача удалена")
    except(IndexError, ValueError):
        update.message.reply_text("необходимо писать: /unset <номер в списке>, например: /unset 1")


def todo_list_view(update, context):
    time_now = datetime.now()

    deleted_tasks = [i for i in context.chat_data if context.chat_data[i]['date'] < time_now.astimezone(utc)]
    for i in deleted_tasks:
        del context.chat_data[i]

    if context.chat_data:
        todo_list_msg = ''
        number = 1

        for i in context.chat_data:
            todo_list_msg += f'{number}. {i.capitalize()}\n'
            number += 1

        if todo_list_msg:
            # update.message.reply_text(text=f'{todo_list_msg}\n'
            # '🗑 Чтобы удалить задачу напиши /unset <номер в списке>')
            keyboard = [[InlineKeyboardButton("🗑 Удалить", callback_data='1')]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(text=f'{todo_list_msg}\n'
                                           '🗑 Чтобы удалить задачу напиши /unset <номер в списке>',
                                      reply_markup=reply_markup)

    else:
        update.message.reply_text(text='У тебя нет задач')

    return CHOOSING


def broadcast_message(update, context):
    if update.message.chat_id == 195177538:
        message_text = update.message.text[11:]
        for i in users_id:
            context.bot.send_message(i, message_text)


def save_users_list(update, context):
    update.message.reply_text(users_id)
    pass


def help():
    pass


def message_set(update, context):
    if update.message.chat_id not in users_id:
        users_id.append(update.message.chat_id)

    local_tz = tz.tzoffset('+3', 10800)
    time_now = datetime.now().astimezone(local_tz)
    task_time = re.search(r'(\d{1,2})(:)(\d{1,2})', update.message.text)
    task_date = re.search(r'(\d{1,2}\.\d{1,2})(\.\d{,4})?', update.message.text)

    if task_time and not re.search(r'(З|завтра)', update.message.text) and not task_date:
        task_time = task_time.group(0).split(':')
        task_time = datetime(time_now.year, time_now.month, time_now.day, int(task_time[0]),
                             int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        if task_time > time_now.astimezone(utc):
            new_timer = context.job_queue.run_once(alarm, task_time, context=update.message.chat_id,
                                                   name=update.message.text)
            context.chat_data[str(update.message.text)] = {'date': task_time, 'job': new_timer}
            update.message.reply_text("Запись внесена в список дел")
        else:
            update.message.reply_text("Это время уже в прошлом...")

    elif task_time and task_date and not re.search(r'(З|завтра)', update.message.text):
        task_time = task_time.group(0).split(':')
        task_date = task_date.group(0).split('.')
        if len(task_date) == 3 and len(task_date[2]) == 4:
            task_time = datetime(int(task_date[2]), int(task_date[1]), int(task_date[0]), int(task_time[0]),
                                 int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        elif len(task_date) == 3 and len(task_date[2]) == 2:
            task_time = datetime(int(task_date[2]) + 2000, int(task_date[1]), int(task_date[0]), int(task_time[0]),
                                 int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        else:
            task_time = datetime(time_now.year, int(task_date[1]), int(task_date[0]), int(task_time[0]),
                                 int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        print(task_time)
        if task_time > time_now.astimezone(utc):
            new_timer = context.job_queue.run_once(alarm, task_time, context=update.message.chat_id,
                                                   name=update.message.text)
            context.chat_data[str(update.message.text)] = {'date': task_time, 'job': new_timer}
            update.message.reply_text("Запись внесена в список дел")
        else:
            update.message.reply_text("Это время уже в прошлом...")

    elif re.search(r'(З|завтра)', update.message.text) and task_time:
        task_time = task_time.group(0).split(':')

        try:
            task_time = datetime(time_now.year, time_now.month, time_now.day + 1, int(task_time[0]),
                                 int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)
        except:
            task_time = datetime(time_now.year, time_now.month + 1, 1, int(task_time[0]),
                                 int(task_time[1]), tzinfo=timezone(timedelta(hours=+3))).astimezone(utc)

        if task_time > time_now.astimezone(utc):
            new_timer = context.job_queue.run_once(alarm, task_time, context=update.message.chat_id,
                                                   name=update.message.text)
            context.chat_data[str(update.message.text)] = {'date': task_time, 'job': new_timer}
            update.message.reply_text("Запись внесена в список дел")

    deleted_tasks = [i for i in context.chat_data if context.chat_data[i]['date'] < time_now.astimezone(utc)]
    for i in deleted_tasks:
        del context.chat_data[i]


def message_null(update, context):
    update.message.reply_text("Необходимо указать время в форате ЧЧ:ММ, дата по желанию")


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# def test(update, context):
#     query = update.callback_query
#     if query.answer():
#         query.edit_message_text(text="Укажите номера задач которые вы хотите удалить")
#
#     return TYPING_CHOICE


# def unset2(update, context):
#     update.message.reply_text("работает")
#     deleted_list = re.findall('(\d{1,2})', update.message.text)
#
#     for i in deleted_list:
#         number = int(i) - 1
#         todo_list = [i for i in context.chat_data]
#         timer = context.chat_data[todo_list[number]]['job']
#         timer.schedule_removal()
#         del context.chat_data[todo_list[number]]
#
#     update.message.reply_text("Задача удалена")

    # print(query.answer())


def location(update, context):
    tf = TimezoneFinder()
    longitude = update.message.location['longitude']
    latitude = update.message.location['latitude']
    local_tz = datetime.now(pytz.timezone(tf.certain_timezone_at(lng=longitude, lat=latitude))).strftime('%Z%z')
    tzzz_hours = int(local_tz[-5:]) // 100
    tzzz_minutes = int(local_tz[-5:]) % 100
    context.chat_data['local_tz'] = {'hours': tzzz_hours, 'minutes': tzzz_minutes}
    update.message.reply_text("Локация сохранена")


def main():
    updater = Updater('1155995478:AAHhthsw8Jm2odjX55UvJ6Y95_GX7S3iOks', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(MessageHandler(Filters.regex(r'(\d{1,2})(:)(\d{1,2})') & ~Filters.location & ~Filters.command, message_set, pass_job_queue=True, pass_chat_data=True))
    # dp.add_handler(MessageHandler(Filters.all & ~(Filters.regex(r'(\d{1,2})(:)(\d{1,2})') & ~Filters.location & ~Filters.command), message_null))
    dp.add_handler(CommandHandler("set", set_timer, pass_args=True, pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))
    dp.add_handler(CommandHandler("todo_list", todo_list_view, pass_chat_data=True))
    dp.add_handler(MessageHandler(Filters.location, location, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("1984_admin", broadcast_message))
    dp.add_handler(CommandHandler("1984_admin_save", save_users_list))
    dp.add_handler(MessageHandler(Filters.location, location, pass_job_queue=True, pass_chat_data=True))

    # dp.add_handler(CommandHandler("test", test))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
