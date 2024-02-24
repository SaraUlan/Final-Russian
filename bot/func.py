


def send_quotes(db):
    row = db.select(table='quotes', limit=1, random = True)
    return f'\"{row[0]['quote']}\"\n{row[0]['author']}'

def add_quotes():
    ...

def send_own_quotes():
    ...

def send_sarma(db):
    row = db.select(table='quotes', limit=1, random = True, condition='author = \'Робин Шарма\'')
    return f'\"{row[0]['quote']}\"\n{row[0]['author']}'

def send_dostoyevski(db):
    row = db.select(table='quotes', limit=1, random = True, condition='author = \'Фёдор Михайлович Достое́вский\'')
    return f'\"{row[0]['quote']}\"\n{row[0]['author']}'

def send_linkoln(db):
    row = db.select(table='quotes', limit=1, random = True, condition='author = \'Авраам Линкольн\'')
    return f'\"{row[0]['quote']}\"\n{row[0]['author']}'

def my_quote(db, author):
    row = db.select(table='quotes', limit=1, random = True, condition=f'author = \'{author}\'')
    return f'\"{row[0]['quote']}\"\n{row[0]['author']}'