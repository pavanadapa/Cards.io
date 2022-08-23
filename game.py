import random
from itertools import cycle

class Card(object):
    def __init__(self, value, suit, trump = None, ptrump = None):
        self.value = value
        self.suit = suit
        self.trump = trump
        self.ptrump = ptrump

    def __repr__(self):
        value_name = ""
        suit_name = ""
        if self.showing:
            if self.value == 0:
                value_name = "Two"
            if self.value == 1:
                value_name = "Three"
            if self.value == 2:
                value_name = "Four"
            if self.value == 3:
                value_name = "Five"
            if self.value == 4:
                value_name = "Six"
            if self.value == 5:
                value_name = "Seven"
            if self.value == 6:
                value_name = "Eight"
            if self.value == 7:
                value_name = "Nine"
            if self.value == 8:
                value_name = "Ten"
            if self.value == 9:
                value_name = "Jack"
            if self.value == 10:
                value_name = "Queen"
            if self.value == 11:
                value_name = "King"
            if self.value == 12:
                value_name = "Ace"
            if self.suit == 0:
                suit_name = "Diamonds"
            if self.suit == 1:
                suit_name = "Clubs"
            if self.suit == 2:
                suit_name = "Hearts"
            if self.suit == 3:
                suit_name = "Spades"
            return value_name + " of " + suit_name
        else:
            return "[CARD]"

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.suit == self.trump and other.suit != self.trump: 
            return True
        elif self.suit == self.trump and other.suit == self.trump:
            if self.value > other.value:
                return True
            else:
                return False
        elif self.suit == self.ptrump and other != self.ptrump: 
            return True
        elif self.suit == self.ptrump and other == self.ptrump: 
            if self.value > other.value:
                return True
            else:
                return False
        else: 
            False
    
    def __lt__(self, other):
        if self.suit == self.trump and other.suit != self.trump: 
            return False
        elif self.suit == self.trump and other.suit == self.trump:
            if self.value > other.value:
                return False
            else:
                return True
        elif self.suit == self.ptrump and other != self.ptrump: 
            return False
        elif self.suit == self.ptrump and other == self.ptrump: 
            if self.value > other.value:
                return False
            else:
                return True
        else: 
            True



class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(i, j)) for j in suits] for i in values]

    def __repr__(self):
        return f"Standard deck of cards\n{len(self)} cards remaining"


    def shuffle(self):
        random.shuffle(self)
        print("\n\n--deck shuffled--")

class deal():
    def __init__(self, numplayers = 4, numcards = 6):
        self.numplayers = numplayers
        self.numcards = numcards
        self.cards = StandardDeck()
        self.hands = cycle([[] for i in range(self.numplayers)])

    def deal(self):
        self.cards.shuffle()
        for x in range(self.numcards*self.numplayers):
            next(self.hands).append(self.cards.pop(0))

def bid(bids):
    return max(bids)

def winningcard(cards):
    return max(cards)


class gamepoints():
    def __init__(self, pile, trump):
        self.pile = pile
        self.trump = trump
        self.maxcard = max(pile)
        self.mincard = None
        self.jack = False
        self.points = 0

    def points(self):
        self.points = 0
        for card in self.pile:
            if card.value == 9:
                self.points +=1
            elif card.value == 10:
                self.points +=2  
            elif card.value == 11:
                self.points +=3
            elif card.value == 12:
                self.points +=4
            elif card.value == 8:
                self.points += 10
            else:
                self.points += 0
    
    def havejack(self):
        if Card(9, self.trump) in self.pile:
            self.jack = True

    def min(self):
        first = True 
        for card in self.pile:
            if card.suit == self.trump and first:
                self.mincard == card
                first = False
            elif card.suit == self.trump:
                if card.value < self.mincard.value:
                    self.mincard == card
                else:
                    pass
            else: pass

class game():
    def __init__(self, numplayers = None, players = None, playtill = None, scores = None, piles = None):
        self.numplayers = numplayers
        self.players = players
        self.playtill = playtill
        self.scores = scores
        self.piles = piles 

    def initialization(self, default = False, numplayers = None, players = None, playtill = None):
        if default == True:
            self.numplayers = 4
            self.players = ["player1", "player2", "player3", "player4"]
            self.playtill = 11
            return None
        if numplayers is not None:
            self.numplayers = numplayers
        if players is not None:
            self.players = players
        if playtill is not None:
            self.playtill = playtill
        if self.numplayers and self.players and self.playtill:
            return None
        if numplayers is None:
            while True:
                self.numplayers =  int(input("Enter Number of Players: "))
                confirmation = input("Are you sure the number of players playing is {p}? (y/N) ".format(p = self.numplayers))
                if confirmation in ["yes", "Yes", "Y", "y", "Yeah", "yeah"]:
                    break
        if players is None: 
            n = 1
            self.players = [[] for i in range(self.numplayers)]
            for i in range(self.numplayers):
                while True:
                    self.players[i] =  input("Enter Player {n}'s name: ".format(n = n))
                    confirmation = input("Are you sure Player {n}'s name is {p}? (y/N) ".format(n = n, p = self.players[i]))
                    if confirmation in ["yes", "Yes", "Y", "y", "Yeah", "yeah"]:
                        n += 1
                        break
        if playtill is None:
            while True:
                self.playtill =  int(input("Enter the number of points to win the game: "))
                confirmation = input("Are you sure the number of points to win the game is {p}? (y/N) ".format(p = self.playtill))
                if confirmation in ["yes", "Yes", "Y", "y", "Yeah", "yeah"]:
                    break
                
                


        

myGame = game()
myGame.initialization()



        