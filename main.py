import telebot
import os
from flask import Flask, request

token = '633492132:AAGL0sgeSSe5zUSYEw05Pu0i6fP8IzYO29w'
server = Flask(__name__)
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def handle_text1(message):

    if message.text == ("Пн"):
        bot.send_message(message.from_user.id, "1. Питон(л)")
        bot.send_message(message.from_user.id, "2. Excel(пр)/Питон(пр)")
        bot.send_message(message.from_user.id, "3. -/Теория вероятности(пр)")
        bot.send_message(message.from_user.id, "4. Теория вероятности(л)")

    elif message.text == "Вт":
        bot.send_message(message.from_user.id, "1. Философия")
        bot.send_message(message.from_user.id, "2. -")
        bot.send_message(message.from_user.id, "3. Excel(л)")

    elif message.text == "Ср":
        bot.send_message(message.from_user.id, "1. Мат анализ(л)")
        bot.send_message(message.from_user.id, "2. -")
        bot.send_message(message.from_user.id, "3. Дифференциальные уравнения(пр)/АСД(пр)")
        bot.send_message(message.from_user.id, "4. Вступление в специальность(л)")
        bot.send_message(message.from_user.id, "5. Физ-ра")


    elif message.text == "Чт":
        bot.send_message(message.from_user.id, "1. Вступление в специальность(пр)")
        bot.send_message(message.from_user.id, "2. Дифф уравнения(л)")

    elif message.text == "Пт":
        bot.send_message(message.from_user.id, "1. Философия(пр)")
        bot.send_message(message.from_user.id, "2. АСД(л)")
        bot.send_message(message.from_user.id, "3. -")
        bot.send_message(message.from_user.id, "4. Мат анализ(пр)")

    else:
        bot.send_message(message.from_user.id, "Введи Пн/Вт/Ср/Чт/Пт")



@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram-bot-s.herokuapp.com/' + token)
    return "CONNECTED", 200

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))