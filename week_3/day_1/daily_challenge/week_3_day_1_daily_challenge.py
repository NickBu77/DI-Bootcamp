# Instructions : Old MacDonald’s Farm

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.

class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals_list = []

    def add_animal(self,animal,number=1):
        self.animals_list.extend([animal] * number)

    def animal_count(self):
        animal_dict = {}
        counter=0
        for a in self.animals_list:
            if a in animal_dict:
                animal_dict[a] += 1
            else:
                animal_dict[a] = 1
        print(f'{self.name}' )
        for k, v in animal_dict.items():
            print(f'{k}: {v}')
        print(' '*10+'E-I-E-I-0!')
        

farm_1 = Farm('Old McDonald')
farm_1.add_animal('sheep',2)
farm_1.add_animal('chicken',5)
farm_1.add_animal('hen')
farm_1.add_animal('rabbit',10)

print(farm_1.name)

print(farm_1.animals_list)
print(farm_1.animal_count())


