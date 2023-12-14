import psycopg2
import os
from dotenv import load_dotenv

# PART 1
# In this exercise we will use PostgreSQL and Python.

load_dotenv()

conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        dbname=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
        )

cur = conn.cursor()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def insert(self):
        try:
            insert_query = 'INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)'
            data_to_insert = (self.name, self.price)
            cur.execute(insert_query, data_to_insert)
            conn.commit()
        except Exception as e: 
            print(e)

    def delete(self):
        delete_query = 'DELETE FROM menu_items where item_name = %s and item_price = %s'
        
        data_to_delete = (self.name, self.price)
        cur.execute(delete_query, data_to_delete)
        conn.commit()

    def update(self, new_name, new_price):
        update_query = 'UPDATE menu_items set item_name = %s, item_price = %s where item_name = %s and item_price = %s'
        data_to_update = (new_name, new_price, self.name, self.price)
        cur.execute(update_query, data_to_update)
        conn.commit()


item = MenuItem('Burger', 35)
item2 = MenuItem('Pizza', 13)
item3 = MenuItem('Cheesecake',25)
# item.insert()
# item2.insert()
# item3.insert()
# item.delete()


cur.execute('DELETE from menu_items where item_price IS NULL')
conn.commit()



# cur.close()
# conn.close()


