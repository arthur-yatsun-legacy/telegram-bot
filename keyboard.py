import telebot

from telegram_bot.main import bot


class Keyboard:

    def __init__(self):
        self.bot = bot

    def main_menu(self, message):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('124-17-1')
        markup.row('124-17-2')
        self.bot.send_message(message.from_user.id, 'Выберите группу:', reply_markup=markup)

    def days(self, message):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('Понедельник', 'Вторник')
        markup.row('Среда', 'Четверг')
        markup.row('Пятница')
        self.bot.send_message(message.from_user.id, 'Выберите день:', reply_markup=markup)

