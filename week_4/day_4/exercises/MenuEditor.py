import psycopg2
import os
from dotenv import load_dotenv
from MenuItems import MenuItem
from MenuManager import MenuManager

#Part 2
# Create a file called menu_editor.py , which will have the following functions:
conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS'),
        dbname=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
        )

cur = conn.cursor()

class menu_editor:

    def show_user_menu(self):
        while True:
            self.response = input(''' 
                   Please type  'V' to view a menu item
                                'A' to add an item to the menu
                                'D' to delete an item
                                'U' to update an item
                                'S' to show the menu
                                'E' to exit
                                 ''')
            if self.response.upper() == 'E':
                self.view_menu()
                break   
            if self.response.upper() == 'V':
                self.view_item()
            elif self.response.upper() == 'A':
                self.insert_item()
            elif self.response.upper() == 'D':
                self.delete_item()
            elif self.response.upper() == 'U':
                self.update_item()            
            elif self.response.upper() == 'S':
                self.view_menu()
            else:
                print('Invalid input. Please enter a valid option.')
            
    def view_item(self):
        item = input('Which item would you like to view: ')
        view = MenuManager()
        row = view.get_by_name(item)
        for r in row:
            print(f'ID: {r[0]}')
            print(f'Menu name: {r[1]}')
            print(f'Menu price: {r[2]}')

    def insert_item(self):
        try:
            item = input('Which item would you like to add: ')
            price = input('What is its price in USD: ')
            add = MenuItem(item, price) 
            add.insert() 
            conn.commit()
            print('Successfully added')
        except Exception as e:
            print(e)
    
    def delete_item(self):
        try:
            item = input('Which item would you like to delete: ')
            cur.execute('SELECT item_price from menu_items where item_name = %s', (item,))
            price = cur.fetchone()[0]
            delete = MenuItem(item, price) 
            delete.delete() 
            # conn.commit()
            print(f'{item} was successfully deleted'.capitalize())
        except Exception as e:
            print(e)

    def update_item(self):
        try:
            item = (input('Which item would you like to update: ')).lower()
            print(f'{item}')
            cur.execute('SELECT item_price from menu_items where item_name = %s', (item,))
            price = cur.fetchone()[0]
            new_name = (input(f'{item.capitalize()} costs {price} USD. What is the new item name?: ')).lower()
            new_price = input(f'What is the new item price in USD?: ')
            update = MenuItem(item, price)
            update.update(new_name, new_price)
            print(f'Successfully updated.')
        except Exception as e:
            print(e)

    def view_menu(self):
        menu = MenuManager()
        items = menu.all()
        for item in items:
            print(f'Item ID {item[0]}, {item[1].lower()} is {item[2]} USD')


ed = menu_editor()
ed.show_user_menu()




#show_user_menu() - this function should display the program menu (not the restaurant menu!), 
#and ask the user to :
# View an Item (V)
# Add an Item (A)
# Delete an Item (D)
# Update an Item (U)
# Show the Menu (S)
# Call the appropriate function that matches the user’s input.

# add_item_to_menu() - this function should ask the user to input the item’s name and price. 
# This function will not interact with the menu itself, but simply create a MenuItem object 
# and call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.

# remove_item_from_menu()- this function should ask the user to input the name of the item they 
# want to remove from the restaurant’s menu. This function will not interact with the menu itself, 
# but simply create a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# update_item_from_menu()- this function should ask the user to input the name and price of the item 
# they want to update from the restaurant’s menu, as well as to input the name and price they want 
# to change them with. This function will not interact with the menu itself, but simply create 
# a MenuItem object and call the appropriate function from the MenuItem object.
# If the item was updated successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# show_restaurant_menu() - print the restaurant’s menu.

# When the user chooses to exit the program, display the restaurant menu and exit the program.