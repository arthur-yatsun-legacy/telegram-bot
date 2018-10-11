import telebot
import os
from flask import Flask, request

token = '633492132:AAGL0sgeSSe5zUSYEw05Pu0i6fP8IzYO29w'
server = Flask(__name__)
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_text(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Получить расписание')
    user_markup.row('Получить расписание по подписке')
    user_markup.row('Время пар')
    user_markup.row('Обновления', 'Обратная связь')
    bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)


@server.route("/")
def web_hook():
    bot.remove_webhook()
    bot.set_webhook(url='https://glacial-lowlands-23073.herokuapp.com/' + token)
    return "CONNECTED", 200

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))