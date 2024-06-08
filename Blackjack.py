import random

suits = ["spades","clubs","diamonds","hearts"]
ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
values = [2,3,4,5,6,7,8,9,10,10,10,10,11]

wins = 0
loses = 0

#classes
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
    
    def take_bet(self,bet):
        self.bet = bet
        self.chips -= bet

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





#functions

def bet(Chips): #processing the bet

    while True:
        try:
            amount = int(input("\nEnter your bet:"))

            if amount > Chips.chips:
                print("\nYOU DO NOT HAVE THAT MANY CHIPS")
            
            else:
                return amount
                break
            
        except:
            print("\nINVALID INPUT, TRY AGAIN.")


def hit():
    pass


def table(Dealer_hand,Player_Hand): #table is the main game 

    global turn

    print("--GAME START--")
    
    while True:

        #the player always goes first, once their turn is over it becomes the dealer's turn, then the game ends and the rewards are given out
        if turn == "player":
            print("\nDealer's hand:",str(Dealer_hand.hand[0])+" -Card Hidden-\n\nPlayer's Hand:",str(Player_Hand.hand)) #dealers second hand is hidden

            try:
                action = int(input("\nEnter action (Enter 1 or 2):\n(1)Hit\n(2)Stand"))

                #player decision
                if input == 1:#hit
                    hit()

                else:#stand
                    turn = "dealer"

            except:
                print("Invalid input")

        else:
            print("\nDealer's hand:",str(Dealer_hand.hand)+"\n\nPlayer's Hand:",str(Player_Hand.hand))


turn = "player"

#main
Deck = Deck(suits,ranks,values)

Chips = Chips()

Dealer_hand = Hand()

Player_Hand = Hand()

print("--WELCOME TO BLACKJACK--")

while True:

    Deck.shuffle()

    print("\nChips:",Chips.chips)

    #get the bet and deduct the bet from the chips
    bet = bet(Chips)
    Chips.take_bet(bet)

    #add 2 cards automatically to both hands
    Dealer_hand.hit(Deck)
    Dealer_hand.hit(Deck)

    Player_Hand.hit(Deck)
    Player_Hand.hit(Deck)

    table(Dealer_hand,Player_Hand)

    break