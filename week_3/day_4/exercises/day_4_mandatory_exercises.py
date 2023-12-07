# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. 
#This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. 
# The length parameter will be used to determine how many words 
# the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
import random

file_path = r"C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\exercises\norvig.txt"

with open(file_path, encoding = 'utf-8', mode='r') as f:
    txt_file= f.readlines() #to get a list of the lines as output


words_list = []

def get_words_from_file(file):
    for list_item in file:
        words_list.append(list_item.strip('\n'))  
    return words_list


def get_random_sentence(length):
    chosen_words = []
    sentence = []
    for i in range(length):
        chosen_words.append(random.choice(words_list).lower())
    sentence = ' '.join(chosen_words)
    return sentence.capitalize()+'.'

length_input = int(input('Enter an integer between 2 and 20: '))

def main(length_input):
    print('This script prints randomly formulated sentences based on your input.')
    length_input = int(length_input)
    try:
        if 2<=length_input<=20 and isinstance(length_input, int):
            length = length_input
    except:
        raise ValueError('Incorrect integer')
    get_words_from_file(txt_file)
    return print(get_random_sentence(length))


main(length_input)

        
# Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{ 
#    "company":{ 
#       "employee":{ 
#          "name":"emma",
#          "payable":{ 
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json

json_file = r'C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\exercises\json_file.json'

with open(json_file,'r') as f:
    worker = json.load(f)

worker['company']['employee']['birth_date']='11/01/1990'

new_worker_data = worker
print(new_worker_data)

with open(json_file, 'w') as f_o:
    json.dump(new_worker_data, f_o)

