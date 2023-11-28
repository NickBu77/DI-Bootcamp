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

print(more_on_zara)
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?