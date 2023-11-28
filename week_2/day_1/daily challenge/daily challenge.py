#Daily Challenge

message = 'give me a random string of 10 characters exactly: '
user_string = input(message)

if len(user_string) ==10:
    print('Perfect')
elif len(user_string) > 10:
    print('Too long. Try again')

elif len(user_string) < 10:
    print('Too short. Try again')


letters=''
for letter in user_string:
    letters += letter
    print(letters)

import random

letters_list = list(letters)

random.shuffle(letters_list)
print(letters_list)














