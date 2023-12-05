# Exercise 1: Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals


    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def make_noise(self):
        for animal in self.animals:
            print(animal.make_noise())

class Cat():
    is_lazy = True

    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    
    def make_noise(self):
        return f'{self.name} is making a {self.sound} noise'

    def walk(self):
        return f'{self.name} is just walking around'
    


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    

bengal_cat = Bengal(name='Ben',age=2,sound='hiss')
chartreux_cat =  Chartreux(name='Char',age=3,sound='meow')
siamese_cat = Siamese(name='Siam',age=7, sound='cry')

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()
sara_pets.make_noise()

#  Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = True

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        running_speed = int(self.weight/self.age*10)
        print(f'{self.name} runs at {running_speed} miles per hour')
        return running_speed

    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            return f'{self.name} is faster than {other_dog.name}'
        else:
            return f'{other_dog.name} is faster than {self.name}'

dog_1 = Dog('Rex',3, 20)
dog_2 = Dog('Lily',5,10)
dog_3 = Dog('Maya', 10, 5)

print(dog_2.bark())
print(dog_3.run_speed())
print(dog_1.fight(dog_2))