#Exercise 1 : Set
#Add two new numbers to the set.
#Remove the last number.

my_fav_numbers = {7,13,18,20,43,21,2022}
friend_fav_numbers = {12,42,11,344,8}

my_fav_numbers.update({33,88})
print(my_fav_numbers)
my_fav_numbers.remove(88)
print(my_fav_numbers)

#Exercise 2: Tuple
#Answer: Tuples are immutable. No adding integers.

#Exercise 3: List

fruits = ["Banana", "Apples", "Oranges", "Blueberries"];


fruits.remove(fruits[0])
fruits.remove('Blueberries')
fruits.append('Kiwi')
fruits.insert(0,'Apples')
print(fruits)
print(fruits.count('Apples'))

#Exercise 4: Floats

#Recap – What is a float? What is the difference between an integer and a float?
#Answer: A float is a number w. atleast one decimal place. An integer is a whole number.

#Can you think of another way to generate a sequence of floats?

number = 0

while number <= 5.5:
    number += .5
    print(number)


#Exercise 5: For Loop
#1
for i in range(1,21,1):
    print(i)
#2
for i in range(1,21,2):
    print(i)

Exercise 6 : While Loop
my_name = 'Nick'
your_name = input('what\'s your name?')

while your_name != my_name:
    your_name = input('what\'s your name?')
    print('try again')
print('great name')


#Exercise 7: Favorite Fruits

user_fruit = input('What\' your favorite fruit, seperated by a space?: ')
user_fruit_a = user_fruit.replace(' ',',')
user_fruit_list = user_fruit_a.split(',')
new_fruit = input('choose a new fruit: ')

if new_fruit in user_fruit_list:
    print('You chose one of your favorites')
else:
    print('You chose a new one')


#Exercise 8: Who Ordered A Pizza ?

active = True
toppings = []

while active:
    answer = input('enter a topping ')
    if answer == 'quit':
        print('ok, goodbye ')
        print(f'your total is {10+(len(toppings)*2.5)} dollars')
        break
    else: 
        print(f"I'll add {answer} right away ")
        toppings.append(answer)

#Exercise 9: Cinemax
inp = input('what is the age of all people who want tickets, seperate by a space: ')
ages = inp.replace(' ',',')
ages_list = list(ages.split(','))
price = 0


for age in ages_list: 
    if int(age) < 3:
        price += 0
    elif int(age) <= 12:
         price += 10
    elif int(age) > 12:
        price += 15

print(price)

#4.A group of teenagers

names = ['phil','angus','rob','leah']
names_enter = []

for name in names:
    age = int(input(f'{name}, how old are you? '))
    if (age < 16) or (age > 21):
        print(f"I'm sorry {name} but you cannot enter")
    else: 
        names_enter.append(name)

if len(names_enter) == 0:
    print(f'sorry, none of you can come in')
else: 
    print(f'these are the people who can enter: {names_enter}')

#Exercise 10 : Sandwich Orders


sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while 'Pastrami sandwich' in sandwich_orders :
        sandwich_orders.remove('Pastrami sandwich')

print(sandwich_orders)

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
 


print(finished_sandwiches)
for sandwich in finished_sandwiches:
    sandwich_orders.remove(sandwich)

print(sandwich_orders)







#We need to prepare the orders of the clients:
#Create an empty list called finished_sandwiches.
#One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
#After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
#I made your tuna sandwich
#I made your avocado sandwich
#I made your egg sandwich
#I made your chicken sandwich




