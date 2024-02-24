from psycopg2 import IntegrityError
from database.config import host, user, password, db_name
from database.db import Database
import json

def main():

    file_path = 'jsons/linkoln.json'

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    db = Database(host, user, password, db_name)
    
    for record in data:
        record['author'] = 'Робин Шарма'
        db.insert('quotes', record)
    



if __name__ == '__main__':
    main()

