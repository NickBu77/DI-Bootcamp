class Computer():

    def __init__(self):
        self.name = "Apple Computer" # public
        self.__max_price = 900 # private

    def sell(self):            # public method
        print(f"Selling Price: {self.__max_price}")

    def __sell(self):          # private method
      print('This is private method')

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()


c.sell()
c.set_max_price(500)
c.sell()

\

class Person:
  def __init__(self, name, lastName):
      self.name = name
      self.lastName = lastName

  def __repr__(self):
      return f"{self.__class__.__name__} : {self.name} {self.lastName}"

  def __add__(self, otherf):
      return Person(self.name, otherf.lastName)

father = Person('John', 'Snow')
mother = Person('Kaleesi', 'MotherOfDragons')
# using the __add__() method
dragonChild = father + mother 

print(dragonChild)
# >> Person : John MotherOfDragons // __add__ is called to add two objects

print(type(dragonChild))
# >> <class '__main__.Person'>

# 1 Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # def str(self):
    #     print(f'{self.amount} {self.currency}s')

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if isinstance(other, int):
            int(self.amount) + other
        elif self.currency == other.currency:
            int(self.amount) + other.amount
        else:
            raise TypeError('currencies don\'t match')
        

    
# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#>>> str(c1)
# '5 dollars'
print(str(c1))

# >>> int(c1)
# 5
print(int(c1))

# >>> repr(c1)
# '5 dollars'
print(repr(c1))

# >>> c1 + 5
# 10
print(c1+5)

# >>> c1 + c2
# 15
print(c1+c2)

# >>> c1 
# 5 dollars
# print(c1)

# # >>> c1 += 5
# # >>> c1
# # 10 dollars
# c1 += 5
# print(c1)


# # >>> c1 += c2
# # >>> c1
# c1 += 5
# print(c1)

# # >>> c1 + c3
# # TypeError: Cannot add between Currency type <dollar> and <shekel>
# print(c1+c3)

# Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string
import random

def gen_randon_strings(num):
    letter = string.ascii_letters
    lst = []
    for _ in range(num):
        letters = random.choice(letter)
        lst.append(letters)
    return ''.join(lst)

print(gen_randon_strings(5))