from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
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
    def __init__(self):
        self.hand = []
        
    def add_card(self, card):
        self.hand.append(card)
        
    def remove_cards(self):
        self.hand.clear()

class Player:
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
        self.hand.add_card(self.cards.pop(0))
        self.hand.add_card(self.cards.pop(1))
        self.hand.add_card(self.cards.pop(2))
        self.hand.add_card(self.cards.pop(3))
        return(self.hand.hand[4])

# Play game

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
        my_card = player1.play_card()
        pc_card = player2.play_card()
        num1 = RANKS.index(my_card[0])
        num2 = RANKS.index(pc_card[0])
        if num1 > num2:
            print("You won! Collect your cards!")
            player1.cards.extend(player2.hand.hand)
            player1.cards.extend(player1.hand.hand)
            player1.hand.remove_cards()
            player2.hand.remove_cards()
            play_war()
        elif num2 > num1:
            print("You lost!")
            player2.cards.extend(player1.hand.hand)
            player2.cards.extend(player2.hand.hand)
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
                player1.cards.extend(player1.hand.hand)
                player1.hand.remove_cards()
                player2.hand.remove_cards()
                play_war()
            elif war2 > war1:
                print("You lost!")
                player2.cards.extend(player1.hand.hand)
                player2.cards.extend(player2.hand.hand)
                player1.hand.remove_cards()
                player2.hand.remove_cards()
                play_war()
    elif move.casefold() == "check cards":
        player1.check_cards()
        play_war()
    elif move.casefold() == "quit":
        if len(player1.cards) > len(player2.cards):
            print("You won! Thanks for playing!")
            return
        elif len(player2.cards) > len(player1.cards):
            print("You lost... Better luck next time.")
            return
        else:
            return   
    else:
        print("Invalid input, please try again.")
        play_war()
    
    if(len(player1.cards)) == 0:
        print("You have no cards remaining! You lose!")
    elif(len(player2.cards)) == 0:
        print("Your opponent has no cards remaining! You win!")
        
play_war()

