import psycopg2
import os
from dotenv import load_dotenv
from MenuItems import MenuItem

load_dotenv()

conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        dbname=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
        )

cur = conn.cursor()

class MenuManager:
    def all(self):
        select_query = 'SELECT * from menu_items'
        cur.execute(select_query)
        return cur.fetchall()

    def get_by_name(self, item):
        select_query = 'SELECT * from menu_items where lower(item_name)=lower(%s)'
        data_to_select = (item,)
        cur.execute(select_query, data_to_select)
        output = cur.fetchall()
        if len(output) > 0:
            return output
        else: 
            return f'{item} is not on the menu.'.capitalize()
    
item2 = MenuManager()
# print(item2.get_by_name('Beef Stew'))
items = MenuManager()
# print(items.all())

# cur.close()
# conn.close()

