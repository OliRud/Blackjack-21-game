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
    

    def shuffle(self):
        random.shuffle(self.deck)


    def show_deck(self):
        print(self.deck)
    

    def deal_card(self):
        card = self.deck.pop()
        return card



class Chips:

    def __init__(self):
        self.chips = 100 #starting chips
        self.bet = 0
    

    def win(self):
        pass

    def lose(self):
        pass

    def push(self):
        pass



class Hand:

    def __init__(self):
        self.hand = []
        self.value = 0
    
    def hit(self,Deck):
        card = Deck.deal_card()
        self.hand.append(card[0])
        self.value += card[1]

        return self.hand,self.value
    
    def empty(self):
        self.hand = []
        self.value = 0
        



Deck = Deck(suits,ranks,values)
player_hand = Hand()

Deck.shuffle()

print(player_hand.hit(Deck))
print(player_hand.hit(Deck))