import telebot
from telebot import types
from psycopg2 import OperationalError

bot = telebot.TeleBot('1685917442:AAE2S8fI5p_J1rg_P0YoHTP0GaYU4lamtkY')


@bot.message_handler(commands=['start'])
def start(message):
    connection = psycopg2.connect('users.sql')
    cur = connection.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50))')
    connection.commit()
    cur.close()
    connection.close()
    bot.send_message(message.chat.id, f'Добро пожаловать {message.from_user.first_name}!' )
    bot.register_next_step_handler(message, user_name)


@bot.message_handler(commands=['creators'])
def creators(message):
    bot.send_message(message.chat.id, 'Акниет Сара')

@bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['Motivation'])
def buttons(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Цитаты', callback_data='quotes')
    btn2 = types.InlineKeyboardButton('Авторы', callback_data='authors')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Добавить свои цитаты', callback_data='add_quotes')
    markup.row(btn3)
    bot.reply_to(message, 'hello choose', reply_markup=markup)
     

bot.polling(non_stop=True)