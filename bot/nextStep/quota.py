from bote import bot

def write_quote(message, db):
    if message.content_type != 'text':
        bot.send_message(message.chat.id, '**Пожалуйста, введите текст!**', parse_mode='Markdown')
    else:
        quota = message.text
        author = f'@{message.from_user.username}'
        db.insert('authors', {"author" : author})
        db.insert('quotes', {'quote' : quota, 'author' : author})
        bot.send_message(message.chat.id, '**Мы сохранили вашу цитату!**', parse_mode='Markdown')

def add_new_quote(message, db):
    if message.content_type != 'text':
        bot.send_message(message.chat.id, '**Пожалуйста, введите текст!**', parse_mode='Markdown')
    else:
        quota = message.text
        msg = bot.send_message(message.chat.id, 'Введите имя автора')
        bot.register_next_step_handler(msg, add_new_author, db=db, quota=quota)

def add_new_author(message, db, quota):
    if message.content_type != 'text':
        bot.send_message(message.chat.id, '**Пожалуйста, введите текст!**', parse_mode='Markdown')
    else:
        author = message.text
        db.insert('authors', {'author' : author})
        db.insert('quotes', {'quote' : quota, 'author' : author})
        bot.send_message(message.chat.id, '**Мы сохранили вашу цитату!**', parse_mode='Markdown')
        
