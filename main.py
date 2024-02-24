from bote import bot
from telebot import types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import schedule
import time
import psycopg2
from database.db import Database
from database.config import host, user, password, db_name
from bot.func import *
from bot.nextStep.quota import add_new_quote, write_quote

db = Database(host, user, password, db_name)




@bot.message_handler(commands=['start'])
def start_messafe(message):
    bot.send_message(message.chat.id, 'Приветствую вас в нашем уютном уголке мудрости!\n\n 🌟 Здесь ваш дух будет наполняться вдохновением каждый день. Наш Telegram бот готов подарить вам порцию умных цитат, которые будут вас вдохновлять и мотивировать.\n\n Чтобы сделать этот опыт еще ближе к вам, мы предоставляем возможность добавлять свои любимые цитаты. Поделитесь своей мудростью с сообществом, и давайте вместе создадим атмосферу вдохновения!\n\nПрисоединяйтесь, получайте дозу мудрости каждый день и делитесь своим светом с остальными. 🚀✨ \n\n  Мотbвации /motivation \n\n О нас: /info')


@bot.message_handler(commands=['info'])
def info_func(message):
    bot.send_message(message.chat.id, "Приветствуем вас в мире, созданном с любовью и страстью к мудрости! 🌟\n\nО Нас:\n\nМы - команда энтузиастов, которые собрались вместе, чтобы создать этот уникальный уголок вдохновения. Позвольте нам представиться:\n\n🚀 Ақниет Мәулен(SE-2204) Ұлан Сара(SE-2203):\n\n Мы те, кто воплощает идеи в реальность, создавая каждый день новый источник мудрости для вас.\n\n🌈 Наша цель - делиться вдохновением и мудростью. Мы стремимся создать пространство, где каждая цитата зажигает искру в ваших сердцах.  \n\n  Мотbвации /motivation" )



@bot.message_handler(commands=['motivation'])
def buttons(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Цитаты', callback_data='quotes')
    btn2 = types.InlineKeyboardButton('Авторы', callback_data='authors')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Добавить свои цитаты', callback_data='add_quotes')
    btn4 = types.InlineKeyboardButton('Мои цитаты', callback_data='own_quotes')
    btn5 = types.InlineKeyboardButton('Добавить цитату', callback_data='add_new_quotes')
    markup.row(btn5 ,btn3)
    markup.row(btn4)
    bot.reply_to(message, 'Прекрасно! Выбор – это ключ к индивидуальному опыту. 🤔✨\n\nВыберите одну из следующих опций:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_motivation_callback(call):
    if call.data == 'quotes':
        quota = send_quotes(db)
        bot.send_message(call.message.chat.id, quota)
    elif call.data == 'authors':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Робин Шарма', callback_data='Sarma')
        btn2 = types.InlineKeyboardButton('Авраам Линкольн', callback_data='Linkoln')
        btn3 = types.InlineKeyboardButton('Фёдор Михайлович Достое́вский', callback_data='dostoyevski')
        btn4 = types.InlineKeyboardButton('Назад', callback_data='back')
        markup.row(btn1, btn2)
        markup.row(btn3)
        markup.row(btn4)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
        
    elif call.data == 'add_quotes':
        bot.send_message(call.message.chat.id, 'Введите вашу цитату')
        bot.register_next_step_handler(call.message, write_quote, db)
    elif call.data == 'own_quotes':
        user_username = call.message.chat.username
        quota = my_quote(db, f'@{user_username}')
        bot.send_message(call.message.chat.id, quota)
    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton('Цитаты', callback_data='quotes')
        btn2 = types.InlineKeyboardButton('Авторы', callback_data='authors')
        markup.row(btn1, btn2)
        btn3 = types.InlineKeyboardButton('Добавить свои цитаты', callback_data='add_quotes')
        btn4 = types.InlineKeyboardButton('Мои цитаты', callback_data='own_quotes')
        markup.row(btn3)
        markup.row(btn4)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == 'Sarma':
        quota = send_sarma(db)
        bot.send_message(call.message.chat.id, quota)
    elif call.data == 'Linkoln':
        quota = send_linkoln(db)
        bot.send_message(call.message.chat.id, quota)
    elif call.data == 'dostoyevski':
        quota = send_dostoyevski(db)
        bot.send_message(call.message.chat.id, quota)
    elif call.data == 'add_new_quotes':
        bot.send_message(call.message.chat.id, 'Введите цитату')
        bot.register_next_step_handler(call.message, add_new_quote, db)
        
if __name__=='__main__':

    bot.infinity_polling()
