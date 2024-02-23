import telebot
from telebot import types

bot = telebot.TeleBot('1685917442:AAE2S8fI5p_J1rg_P0YoHTP0GaYU4lamtkY')

@bot.message_handler(commands=['start'])
def start_messafe(message):
    bot.send_dice(message.chat.id)
    bot.send_message(message.chat.id, 'Привет!')


@bot.message_handler(commands=['info'])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text = 'go to the site', url = 'https://www.youtube.com/watch?v=ilpTcZevGYc')
    keyboard.add(url_button)
    url_button = types.InlineKeyboardButton(text = 'go to the site', url = 'https://www.youtube.com/watch?v=ilpTcZevGYc')
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "press btn",reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__=='__main__':
    bot.infinity_polling()
