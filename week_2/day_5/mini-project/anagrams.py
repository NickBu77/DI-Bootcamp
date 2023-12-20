from anagram_checker import AnagramChecker


# def menu():
#     print('Welcome to Anagram Checker! This system allows you to check words\' anagrams and has several exciting features.')
#     user_inp = input('Please enter a word to see all anagrams of this word. If you aren\'t interested, type \'exit.\' ')
#     AnagramChecker.is_valid_word(user_inp)

def main():
    path = r'C:\Users\97258\Documents\DI-Bootcamp\week_3\day_4\exercises\norvig.txt' 
    anagram_checker = AnagramChecker(path)
    # anagram_checker.open_file()

    while True:
        print("Welcome to Anagram Checker! This system allows you to check words\' anagrams and has several exciting features.")
        user_inp = input('Please enter a word to see all anagrams of this word. If you aren\'t interested, type \'exit.\' ').lower().strip()
        print(f"You entered '{user_inp}'")

        if user_inp == "exit":
            print("Exited. Have a good day.")
            break 
        elif ' ' in user_inp:
            print("Error: Please enter in one word.")
            continue

        if not user_inp.isalpha():
            print("Error: Please enter only alpha characters.")
            continue
        else:
            user_inp 
            word = user_inp
            anagram_checker.open_file()
            result = anagram_checker.is_valid_word(word.lower())
            if result == 'This is a valid word.':
                anagram_checker.randomator()
                anagramed_word = anagram_checker.anagrams_for_word(word)
                print(f"Anagrams for {word}: {', '.join(anagramed_word)}")
            else:
                return result


if __name__ == "__main__":
    main()


    

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