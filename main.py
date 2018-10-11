import telebot
import os
from flask import Flask, request
# from telegram_bot import keyboard

token = '633492132:AAGL0sgeSSe5zUSYEw05Pu0i6fP8IzYO29w'
server = Flask(__name__)
bot = telebot.TeleBot(token)

# orgainizer = 0
#
@bot.message_handler(commands=['start'])
def main_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.row('124-17-1')
    markup.row('124-17-2')
    bot.send_message(message.from_user.id, 'Выберите группу:', reply_markup=markup)
#
#
# @bot.message_handler(func=lambda mess: "124-17-1" == mess.text, content_types=['text'])
# def handle_text(message):
#     orgainizer = 1
#     keyboard.days(message)
#
#
# @bot.message_handler(func=lambda mess: "Понедельник" == mess.text, content_types=['text'])
# def handle_text(message):
#     if orgainizer == 1:
#         bot.send_message(message.from_user.id, "1. Питон(л)\n2. - / ТЙМС(пр)\n3. - / CМП(пр)\n4.ТЙМС(л)")
#     elif orgainizer == 2:
#         bot.send_message(message.from_user.id, "1. Питон(л)")
#         bot.send_message(message.from_user.id, "2. Excel(пр)/Питон(пр)")
#         bot.send_message(message.from_user.id, "3. -/Теория вероятности(пр)")
#         bot.send_message(message.from_user.id, "4. Теория вероятности(л)")


@bot.message_handler(content_types=["text"])
def handle_text1(message):

    if message.text == "2Пн":
        bot.send_message(message.from_user.id, "1. Питон(л)")
        bot.send_message(message.from_user.id, "2. Excel(пр)/Питон(пр)")
        bot.send_message(message.from_user.id, "3. -/Теория вероятности(пр)")
        bot.send_message(message.from_user.id, "4. Теория вероятности(л)")

    elif message.text == "1Пн":
        bot.send_message(message.from_user.id, "1. Питон(л)\n2. - / ТЙМС(пр)\n3. - / CМП(пр)\n4.ТЙМС(л)")

    elif message.text == "2Вт":
        bot.send_message(message.from_user.id, "1. Философия")
        bot.send_message(message.from_user.id, "2. -")
        bot.send_message(message.from_user.id, "3. Excel(л)")

    elif message.text == "1Вт":
        bot.send_message(message.from_user.id, "1. СУК\n2. ПЗЕОМ(пр) / -\n3. ПЗЕОМ(л)")

    elif message.text == "2Ср":
        bot.send_message(message.from_user.id, "1. Мат анализ(л)")
        bot.send_message(message.from_user.id, "2. -")
        bot.send_message(message.from_user.id, "3. Дифференциальные уравнения(пр)/АСД(пр)")
        bot.send_message(message.from_user.id, "4. Вступление в специальность(л)")
        bot.send_message(message.from_user.id, "5. Физ-ра")

    elif message.text == "1Ср":
        bot.send_message(message.from_user.id, "1. Мат анализ(л)\n2. -\n3. АСД(пр) / -\n4.Вступ до фаху(л) / -\n5. Физ-ра")

    elif message.text == "2Чт":
        bot.send_message(message.from_user.id, "1. Вступление в специальность(пр)")
        bot.send_message(message.from_user.id, "2. Дифф уравнения(л)")

    elif message.text == "1Чт":
        bot.send_message(message.from_user.id, "1. Диффуры(пр) / Вступ до фаху(пр)\n2. Диффуры(л)")

    elif message.text == "2Пт":
        bot.send_message(message.from_user.id, "1. Философия(пр)")
        bot.send_message(message.from_user.id, "2. АСД(л)")
        bot.send_message(message.from_user.id, "3. -")
        bot.send_message(message.from_user.id, "4. Мат анализ(пр)")

    elif message.text == "1Пт":
        bot.send_message(message.from_user.id, "1. Философия(пр)\n2. АСД(л)\n3. -\n4. Мат анализ(пр)")

    else:
        bot.send_message(message.from_user.id, "Введи в формате\n1Пн - рассписание на понедельник для первой группы\n"
                                               "2Пн - расписание на понедельник для второй группы")


@server.route('/' + token, methods=['POST'])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "POST", 200


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-bot-s.herokuapp.com/' + token)
    return "CONNECTED", 200

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))