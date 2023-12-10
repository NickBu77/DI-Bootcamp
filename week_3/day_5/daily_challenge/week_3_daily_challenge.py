# Part 1: Quiz

# What is a class? A class is a blueprint that contains a number of related functions(methods) w/in it
# What is an instance? An nstance is a specific example you run through the class. For example, a car company may have nultiple instances for every car in class Brand.
# What is encapsulation? This creates private attributes using underscores. It is to restrict modification of the data.
# What is abstraction? This refers to the idea that features and functions like len() in python have code that runs in the background, yet we abstract away these details and to make our lives easier use these functions to avoid having to do these functions manually using for loops, while loops, etc...
# What is inheritance? It is when child classes take on the methods of the parent to avoid having to repeat these methods.
# What is multiple inheritance? A child class can have two different parents. If both have the same operation, the operation from the class lower in the script will override the higher.
# What is polymorphism? Polymorphism is when you have the same function defined in two different classes. Depending on the class specified when the instance is defined, that's the output you'll see once ran.
# What is method resolution order or MRO? This determines the order in which methods have priorities within class families.


# Part 2: Create A Deck Of Cards Class.
import random

class Deck:
    def __init__(self) -> None:
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
    
    def create_cards(self):
        self.cards = [value + ' of ' + suit for suit in self.suits for value in self.values]

    def shuffle_cards(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            print(f'You have {len(self.cards)} cards. That\'s an issue.')

    def deal(self):
        dealt_card = random.choice(self.cards)
        self.cards.remove(dealt_card)
        print(f'You were given the {dealt_card}.')
        print(f'You have {len(self.cards)} cards left in the deck.')

    

deck_1 = Deck()
deck_1.create_cards()
deck_1.shuffle_cards()
deck_1.deal()
