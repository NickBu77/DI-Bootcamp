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
