#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        self.cards = []
        for s in SUITE: 
            for r in RANKS:
                self.cards.append([r, s])
          
    def shuffle(self):
        shuffle(self.cards)
        
    def cut(self):
        self.cards = self.cards[:26], self.cards[26:]

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    
    def __init__(self):
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)
        
    def remove_cards(self):
        self.hand.clear()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    
    def __init__(self, name, cards, hand):
        self.name = name
        self.cards = cards
        self.hand = hand

    def play_card(self):
        print("{name} has played {c}.".format(name = self.name, c = self.cards[0]))
        self.hand.add_card(self.cards.pop(0))
        return(self.hand.hand[0])
    
    def check_cards(self):
        print("{name} has {rem} cards remaining.".format(name = self.name, rem = len(self.cards)))
    
    def play_war(self):
        self.hand.add_card(self.cards.pop(1, 2, 3, 4))
        return(self.hand.hand[5])


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
my_deck = Deck()
my_deck.shuffle()
my_deck.cut()

player1 = Player(input('What is your name? '), my_deck.cards[0], Hand())
player2 = Player("Computer", my_deck.cards[1], Hand())
print("Hello {name}, you have {rem} cards remaining.".format(name = player1.name, rem = len(player1.cards)))

def play_war():
    move = input("What would you like to do? Please type 'Play card', 'Check cards', or 'Quit': ")
    if move.casefold() == "play card":
        print(player1.hand.hand)
        my_card = player1.play_card()
        pc_card = player2.play_card()
        num1 = RANKS.index(my_card[0])
        num2 = RANKS.index(pc_card[0])
        if num1 > num2:
            print("You won! Collect your cards!")
            player1.cards.extend(player2.hand.hand)
            player1.hand.remove_cards()
            player2.hand.remove_cards()
            play_war()
        elif num2 > num1:
            print("You lost!")
            player2.cards.extend(player1.hand.hand)
            player1.hand.remove_cards()
            player2.hand.remove_cards()
            play_war()
        elif num1 == num2:
            print("War! Play 4 more cards!")
            war_card1 = player1.play_war()
            war_card2 = player2.play_war()
            war1 = RANKS.index(war_card1[0])
            war2 = RANKS.index(war_card2[0])
            if war1 > war2:
                print("You won! Collect your cards!")
                player1.cards.extend(player2.hand.hand)
                player1.hand.remove_cards()
                player2.hand.remove_cards()
                play_war()
            elif war2 > war1:
                print("You lost!")
                player2.cards.extend(player1.hand.hand)
                player1.hand.remove_cards()
                player2.hand.remove_cards()
                play_war()
        
    elif move.casefold() == "check cards":
        player1.check_cards()
        play_war()
    elif move.casefold() == "quit":
        return   
    else:
        play_war()
        
play_war()


# Use the 3 classes along with some logic to play a game of war!
