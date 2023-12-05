# Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: 
#“dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

from week_3_day_2_mandatory_exercises import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        self.trained = True
        print(self.bark())

    def play(self,*dog_names):
        dogs_joined = ', '.join(dog_names)
        return f'{dogs_joined} all play together'
    
    def do_trick(self):
        trick_1 = f'{self.name} does a barrel roll'
        trick_2 = f'{self.name} shakes your hand'
        trick_3 = f'{self.name} plays dead'
        tricks_list = [trick_1, trick_2, trick_3]
        if self.trained == True:
            return random.choice(tricks_list)



    

dog_1 = PetDog('Rex',10,20)
dog_2 = PetDog('Maya',15,5)
print(dog_1.play('RyGuy', 'Limor', 'Liam'))
dog_1.fight(dog_2)
dog_1.train()
print(dog_1.trained)
print(dog_1.do_trick())





