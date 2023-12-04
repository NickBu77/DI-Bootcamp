# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


Whiskers = Cat('Whiskers',3)
Mittens = Cat('Mittens',5)
Felix = Cat('Felix',2)

all_cats=[Whiskers, Mittens, Felix]


oldest = [Whiskers]
def oldest_cat(cat_list=all_cats):
    for cat in cat_list:
        if cat.age > oldest[0].age:
            oldest[0]=cat

oldest_cat(all_cats)
print(f'The oldest cat is {oldest[0].name} and is {oldest[0].age} years old.')

# Exercise 2 : Dogs
    
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        return f'The dog, {self.name}, goes woof, woof'
    
    def jump(self,height):
        return f'The dog, {self.name}, jumps {height*2} cm'

Roger = Dog('Roger',17)
Spot = Dog('Spot',19)
RyDog = Dog('RyDog',22)
davids_dog = Dog('Rex',25)
sarahs_dog = Dog('Teacup',20)

print(f'David has a dog called {davids_dog.name} and he is {davids_dog.height} cm tall')
print(f'Sarah has a dog called {sarahs_dog.name} and he is {sarahs_dog.height} cm tall')

if sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} is taller than {davids_dog.name}')
elif  davids_dog.height > sarahs_dog.height:
    print(f'{davids_dog.name} is taller than {sarahs_dog.name}')
else: 
    print('Both dogs are equally tall')

# Exercise 3 : Who’s The Song Producer?

class Song():
    def __init__(self, name, lyrics):
        self.name = name
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

Stairway = Song("stairway",["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])

Stairway.sing_me_a_song()


# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_name(self, *new_animal):
        for animal in new_animal:
            if animal in self.animals:
                print('already in zoo')
            else:
                self.animals.append(animal)
    
    def animal_sold(self,*sold_animal):
        for animal in sold_animal:
            if animal not in self.animals:
                print('not in zoo')
            else:
                self.animals.remove(animal)
    
    def sort_animals(self):
        sorted_animals = self.animals
        self.letter_groupings = {}
        counter = 0
        for animal in sorted_animals:
            first_letter = animal[0]
            if first_letter not in self.letter_groupings:
                self.letter_groupings.update({first_letter:[animal]})
            else:
                self.letter_groupings[first_letter].append(animal)

    def get_groups(self):
        sorted_letters = {key: self.letter_groupings[key] for key in sorted(self.letter_groupings)}
        keys_to_delete = []
        new_keys = []
        for k in sorted_letters.keys():
            keys_to_delete.append(k)
        for i in range(len(keys_to_delete)):
            sorted_letters[i+1] = sorted_letters[keys_to_delete[i]]
        for key in keys_to_delete:
            del sorted_letters[key]
        return sorted_letters

        





zoo_1 = Zoo('NicksZoo')
zoo_1.add_name('giraffe','cat','monkey','elephant','lizard','eel','eke','ladybug')
zoo_1.animal_sold('cat','porcupine')
print(zoo_1.animals)
print(zoo_1.sort_animals())
print(zoo_1.get_groups())

# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)