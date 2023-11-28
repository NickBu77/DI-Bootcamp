#Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dic = dict(zip(keys,values))
print(dic)

# Exercise 2 : Cinemax

#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
keys = list(family)
values = list(family.values())
prices = []

#How much does each family member have to pay ?

#rint out the family’s total cost for the movies.
#Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

for key, value in family.items():
    if value < 3:
        price = 0
        prices.append(price)
    if value <= 12:
        price = 10
        prices.append(price)
    else:
        price = 15
        prices.append(price)
    print(f'{key.capitalize()} is {value} years old and therefore pays {price}')

print(f'The sum for the whole family is {sum(prices)}')

# Exercise 3: Zara

brand = {'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color': 
     {'France': 'blue', 
     'Spain': 'red', 
    'US': ['pink', 'green']}}

print(brand)

brand['number_stores'] = 2

print(f"The prestigious {brand['name']} has {len(brand['type_of_clothes'])} types of customer lines for the demographics {', '.join(brand['type_of_clothes'])} from the following countries: {', '.join(brand['major_color'].keys())}")

brand['country_creation']='Spain'

for key, value in brand.items():
    if key == 'international_competitors':
        ic = brand['international_competitors']
        ic.append('Desigual')
    else:
        continue

#7
del brand['creation_date']

#8
print(brand['international_competitors'][-1])

#9
print(brand['major_color']['US'])

#10
print(len(brand.keys()))

#11
print(brand.keys())

#12
more_on_zara= {'creation_date': 1975, 
'number_stores':10000}

#13
brand.update(more_on_zara)

print(brand)

#14
print(brand['number_stores']) #it printed the new value I added in step 12, overriding the prior value

# Exercise 4 : Disney Characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#1
user_dic = {}
for (i, user) in enumerate(users):
    user_dic[user]=i

print(user_dic)

#2

no2_user_dic={}
for (i, user) in enumerate(users):
    no2_user_dic[i]=user

print(no2_user_dic)

#3

sorted_users = sorted(users)
sorted_dic = {}
for (i, user) in enumerate(sorted_users):
    sorted_dic[user]=i
print(sorted_dic)

#4
disney_users_A=[]
for user in users:
    if 'i' in user:
        disney_users_A.append(user)
    else: 
        continue
print(disney_users_A)

disney_users_A=[]
for user in users:
    if 'm' or 'p' in user.lower():
        disney_users_A.append(user)
    else: 
        continue
print(disney_users_A)

print(15000/4*12)