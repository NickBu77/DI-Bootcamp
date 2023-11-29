# Instructions
# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

word = input('give me a word: ')
word_dict = {}
additional_info ={}
for i, letter in enumerate(word):
    if letter not in additional_info.keys():
        additional_info[letter]=[i]
        word_dict.update(additional_info)
    else:
        additional_info[letter].append(i) 
        word_dict.update(additional_info)     

print(word_dict)

#Challenge 2: 


items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
walletwosigns = int(wallet.replace('$',''))

items_list = list(items_purchase)
costs_list = list(items_purchase.values())

zipped_dict = sorted(list(zip(items_list,costs_list)))
unzipped_dict = dict(zipped_dict)
purchased_amt = []
purchased_item = []


while sum(purchased_amt) < walletwosigns:
    for item, price in unzipped_dict.items():
        price = price.replace('$','')
        if ',' in price:
            price = price.replace(',','')  
        price = int(price)
        if sum(purchased_amt)+price <= walletwosigns:
            purchased_amt.append(price)
            purchased_item.append(item)
        else: 
            continue


print(purchased_item)




