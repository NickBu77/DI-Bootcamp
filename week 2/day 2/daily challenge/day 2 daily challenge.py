#1 

num =  int(input('Give me a number: '))
length = int(input('Give me a length: '))

for i in range(num, length+1, num):
    print(i)


#2

word = input('give me a word ')
letters = []

for letter in word:
    if letter not in letters:
        letters.append(letter)
    else:
        continue

joined_letters = ''.join(letters)
print(joined_letters)
