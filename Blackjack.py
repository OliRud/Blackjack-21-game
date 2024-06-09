import random
import time

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


    def show_deck(self): #for debug(not used)
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
        self.chips += (self.bet * 2)
        print("\nYOU WIN",str(self.bet),"CHIPS")
        self.bet = 0

    def lose(self):
        print("\nYOU LOSE")
        self.bet = 0

    def push(self):
        self.chips += self.bet
        print("\nPUSH")
        self.bet = 0



class Hand:

    def __init__(self):
        self.hand = []
        self.value = 0
        self.bust = False
    
    def hit(self,Deck):
        card = Deck.deal_card()

        if card[1] == 11 and self.value > 11: #convert aces to 1 if the value of the hand is over 11
            card[1] = 1

        self.hand.append(card[0])
        self.value += card[1]

        if self.value > 21:
            self.bust = True

        return self.hand,self.value
    
    def empty(self):
        self.hand = []
        self.value = 0
        self.bust = False





#functions

def bet(): #processing the bet

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


def endgame(Dealer_hand,Player_hand): #calculates the winner

    if Player_hand.bust == True:
        Chips.lose()
    elif Dealer_hand.bust == True:
        Chips.win()
    elif Dealer_hand.value > Player_hand.value:
        Chips.lose()
    elif Dealer_hand.value < Player_hand.value:
        Chips.win()
    elif Dealer_hand.Value == Player_hand.value:
        Chips.push()
    
    print("\nCurrent Chips:",Chips.chips)
    input("\nPress enter to play again")
    


def table(Dealer_hand,Player_hand,Deck): #table is the main game 

    global turn

    print("--GAME START--")
    
    while True:

        #the player always goes first, once their turn is over it becomes the dealer's turn, then the game ends and the rewards are given out
        if turn == "player":
            print("\nDealer's hand:",str(Dealer_hand.hand[0]),"-Card Hidden-\n\nPlayer's Hand:",str(Player_hand.hand),str(Player_hand.value)) #dealers second hand is hidden

            try:
                action = int(input("\nEnter action (Enter 1 or 2):\n(1)Hit\n(2)Stand\n"))

                #player decision
                if action == 1:#hit

                    print("\n-You Hit-\n")
                    
                    Player_hand.hit(Deck)

                    if Player_hand.bust == True:
                        print("\n-PLAYER BUST-\n")
                        turn = "dealer"

                else:#stand
                    turn = "dealer"

            except:
                print("Invalid input")

        #dealer
        elif turn == "dealer":

            print("\n-Dealer's turn-\n")

            print("\nDealer's hand:",str(Dealer_hand.hand),str(Dealer_hand.value)+"\n\nPlayer's Hand:",str(Player_hand.hand))

            time.sleep(1)

            if Player_hand.bust == False and Dealer_hand.value < 16:

                Dealer_hand.hit(Deck)
                time.sleep(1)
            
            else:
                
                endgame(Dealer_hand,Player_hand)
                break


turn = "player"

Deck = Deck(suits,ranks,values)

Chips = Chips()

Dealer_hand = Hand()

Player_hand = Hand()

print("--WELCOME TO BLACKJACK--")
print("\nChips:",Chips.chips)

#main loop
while True:

    Deck.__init__(suits,ranks,values) #replenish the deck every new game

    Player_hand.empty() #empty the hands every new game
    Dealer_hand.empty()

    Deck.shuffle() #shuffle the deck every new game

    #get the bet and deduct the bet from the chips
    bet = bet()
    Chips.take_bet(bet)

    #add 2 cards automatically to both hands
    Dealer_hand.hit(Deck)
    Dealer_hand.hit(Deck)

    Player_hand.hit(Deck)
    Player_hand.hit(Deck)

    table(Dealer_hand,Player_hand,Deck)