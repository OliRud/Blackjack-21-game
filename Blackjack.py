import random

suits = ["spades","clubs","diamonds","hearts"]
ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]

wins = 0
loses = 0

class Deck:
    
    def __init__(self,suits,ranks,values):
        self.deck = []
    
        for suit in suits:

            value = 0

            for x in ranks:
                card = x + " of " + suit
                self.deck.append([card,values[value]]) #ive chosen to store the cards in a 2d array, each block having the card name paired with its value
                value += 1
    
    def show_deck(self):
        print(self.deck)
    

Deck = Deck(suits,ranks,values)
Deck.show_deck()