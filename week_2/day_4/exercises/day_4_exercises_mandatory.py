#Exercise 1 : What Are You Learning ?
def display_message(message):
    return print(message)

message = "I am learning full stack"
display_message(message)

# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title:str):
    return print(f'One of my favorite books is {title}')

title = 'Alice in Wonderland'
favorite_book(title)

# Exercise 3 : Some Geography
def describe_city(city:str, country:str):
    return f'{city} is in {country}'

city= 'Reykjavik'
country = 'Iceland'
print(describe_city(city, country))

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def rand():
    no = input('Give me a number from 1 to 100: ')
    second_no = random.randint(1, 100)
    if no == second_no:
        print(f'Great success. Your number {no} matches.')
    else:
        print(f'Sorry mami. You chose {no}. You should have chosen {second_no}.')

rand()

# Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message

def make_shirt(size: float = 5, text: str= 'I love Python'):
    return f'The size of the shirt is {size} and the text is \'{text}\''

print(make_shirt())
print(make_shirt(3,"Let's code!"))
print(make_shirt(1,"Coding is cool"))

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(*kwargs, size=5, text='I love Python'):
    return f'The size of the shirt is {size} and the text is \'{text}\''

print(make_shirt())
print(make_shirt(size=3,text="Let's code!"))
print(make_shirt(size=1,text="Coding is cool"))

# Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# a,b,c = magician_names

def show_magicians(magician_names:list):
    for name in magician_names:
        print(name)

show_magicians(magician_names)

def make_great(magician_names:list):
    for i, name in enumerate(magician_names):
        magician_names[i] = "the Great "+name
    return magician_names
    
print(make_great(magician_names))

# Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

import random

def get_random_temp(season: input):
    if season == 'winter':
        return random.randint(-10,16)
    elif season == 'spring':
        return random.randint(17, 23)
    else:
        return random.randint(24, 40)


print(get_random_temp(season=input('What is the season? ')))


# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    temp = get_random_temp(input('What is the season? '))
    print( f'The temperature right now is {temp} degrees ')
    if temp < 0:
        return "Brrr, that’s freezing! Wear some extra layers today"
    elif temp <= 16:
        return "Chilly. Bring a coat"
    elif temp <= 23:
        return "It's warm. Wear a t-shirt."
    elif temp <= 32:
        return "Hot! Bring suntan"

# print(main())

# Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

questions_answers= [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers


questions =[]
answers =[]

for QnAs in questions_answers[0:]:
    for key, value in QnAs.items():
        if key == "question":
            questions.append(value)
        elif key == "answer":
            answers.append(value)

# take_quiz(questions=QnA[])

correct_answers= []
wrong_answers = []
new_dict = {}

new_dict = dict(zip(questions,answers))
#print(new_dict)

def quiz(new_dict:dict=new_dict):
    for q,a in new_dict.items():
        user_answer = input(q+' ').lower()
        if user_answer == a.lower():
            print('That\'s right')
            correct_answers.append(q)
        else:
            print('That\'s wrong. You fail.')
            wrong_answers.append(q)
        print(f'you answered {len(correct_answers)} questions correctly')
        print(f'you answered {len(wrong_answers)} questions incorrectly')
        if len(wrong_answers) >3:
            print('Try again please. You answered too many questions wrong')

quiz(new_dict)



# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.