import telebot
from telebot import types

# Токен вашего бота, полученный от BotFather в Telegram
TOKEN = '7133471743:AAHGSeT7uwNWlJps_NNh9iI2YePGYzTWV8Q'

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот-помощник.")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_MN = types.KeyboardButton("Пройти аттестацию МН")
    item_ON = types.KeyboardButton("Пройти аттестацию ОН")
    markup.row(item_MN, item_ON)

    bot.send_message(message.chat.id, "Выберите вариант действия:", reply_markup=markup)


# Обработчик выбора действий
@bot.message_handler(func=lambda message: True)
def handle_action(message):
    if message.text == "Пройти аттестацию МН":
        bot.send_message(message.chat.id, "Вы решили пройти аттестацию МН.")
    elif message.text == "Пройти аттестацию ОН":
        bot.send_message(message.chat.id, "Вы решили пройти аттестацию ОН.")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, воспользуйтесь предложенными вариантами.")


# Запуск бота
bot.polling()