import telebot
from telebot import types

bot = telebot.TeleBot('1685917442:AAE2S8fI5p_J1rg_P0YoHTP0GaYU4lamtkY')

@bot.message_handler(commands=['start'])
def start_messafe(message):
    bot.send_message(message.chat.id, 'Приветствую вас в нашем уютном уголке мудрости!\n\n 🌟 Здесь ваш дух будет наполняться вдохновением каждый день. Наш Telegram бот готов подарить вам порцию умных цитат, которые будут вас вдохновлять и мотивировать.\n\n Чтобы сделать этот опыт еще ближе к вам, мы предоставляем возможность добавлять свои любимые цитаты. Поделитесь своей мудростью с сообществом, и давайте вместе создадим атмосферу вдохновения!\n\nПрисоединяйтесь, получайте дозу мудрости каждый день и делитесь своим светом с остальными. 🚀✨')


@bot.message_handler(commands=['info'])
def info_func(message):
    bot.send_message(message.chat.id, "Приветствуем вас в мире, созданном с любовью и страстью к мудрости! 🌟\n\nО Нас:\n\nМы - команда энтузиастов, которые собрались вместе, чтобы создать этот уникальный уголок вдохновения. Позвольте нам представиться:\n\n🚀 Ақниет Мәулен(SE-2204) Ұлан Сара(SE-2203):\n\n Мы те, кто воплощает идеи в реальность, создавая каждый день новый источник мудрости для вас.\n\n🌈 Наша цель - делиться вдохновением и мудростью. Мы стремимся создать пространство, где каждая цитата зажигает искру в ваших сердцах." )



@bot.message_handler(commands=['motivation'])
def buttons(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Цитаты', callback_data='quotes')
    btn2 = types.InlineKeyboardButton('Авторы', callback_data='authors')
    markup.row(btn1, btn2)
    btn3 = types.InlineKeyboardButton('Добавить свои цитаты', callback_data='add_quotes')
    btn4 = types.InlineKeyboardButton('Мои цитаты', callback_data='own_quotes')
    markup.row(btn3)
    markup.row(btn4)
    bot.reply_to(message, 'Прекрасно! Выбор – это ключ к индивидуальному опыту. 🤔✨\n\nВыберите одну из следующих опций:', reply_markup=markup)

if __name__=='__main__':
    bot.infinity_polling()
