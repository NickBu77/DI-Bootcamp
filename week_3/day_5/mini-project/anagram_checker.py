# Anagram Checker
# We will create a program that will ask the user for a word.
# It will check if the word is a valid English word, and then find all possible anagrams for that word.


# Instructions
# First Download this text file : right click –> Save As
import random
from itertools import permutations
class AnagramChecker:
    def __init__(self, path):
        self.words_list = []
        self.anagram_dict = {}
        # self.distorted_words = 
        with open(path, mode='r') as f:
            self.file_text = f.readlines() #to get a list of the lines as output
            
    def open_file(self):
        for word in self.file_text:
            self.words_list.append(word.strip('\n').lower())

    
    def is_valid_word(self, word):
        if word.lower() in self.words_list:
            return 'This is a valid word.'
        else:
            return 'Sorry, this is not an official English word.'
        
    def randomator(self):
        for word in self.words_list[0:4]:
            perms =[]
            for p in permutations(word):
                word_perms= ''.join(p)
                perms.append(word_perms)
            self.anagram_dict[word] = perms
        return self.anagram_dict
    
    def anagrams_for_word(self, word):
        return self.anagram_dict[word]

    
    def is_anagram(self,word1, word2):
        word1_sorted = sorted(word1)
        word2_sorted = sorted(word2)
        if word1 == word2:
            return f'{word1} and {word2} are the same word. We want an anagram.'.capitalize()
        elif word1_sorted == word2_sorted:
            return f'{word1} and {word2} are anagrams!'.capitalize()
        else:
            return f'{word1} and {word2} are not anagrams.'.capitalize()


path = r'C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\exercises\norvig.txt'

# a1 = AnagramChecker(path)
# a1.open_file()
# # print(a1.is_valid_word('AA'))
# print(a1.randomator())
# print(a1.anagrams_for_word('aahed'))


# The class should have the following methods:
# __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
# is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, 
# the function should return a list containing [“mate”, “tame”, “team”].)

# Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and 
# return True if they contain the same letters (but not in the same order), and False if not.

# Note: None of the methods in the class should print anything.

# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, 
# and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. 
# (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.

# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.