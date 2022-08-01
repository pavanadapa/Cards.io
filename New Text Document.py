import random
from itertools import cycle

class Card(object):
    def __init__(self, value, suit, trump = None, psuedotrump = None, team = None):
        self.value = value
        self.suit = suit
        self.showing = True
        self.trump = trump
        self.psuedotrump = psuedotrump
        self.team = None


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

    def __lt__(self, other):
        if self.suit == self.trump and other.suit != self.trump:
            return False
        if self.suit != self.trump and other.suit == self.trump:
            return True
        if self.suit == self.trump and other.suit == self.trump:
            if self.value < other.value:
                return True
            else:
                return False
        if self.suit == self.psuedotrump and other.suit != self.psuedotrump:
            return False
        if self.suit != self.psuedotrump and other.suit == self.psuedotrump:
            return True
        if self.suit == self.psuedotrump and other.suit == self.psuedotrump:
            if self.value < other.value:
                return True
            else:
                return False
        else: return False
    def __gt__(self, other):
        if self.suit == self.trump and other.suit != self.trump:
            return True
        if self.suit != self.trump and other.suit == self.trump:
            return False
        if self.suit == self.trump and other.suit == self.trump:
            if self.value < other.value:
                return False
            else:
                return True
        if self.suit == self.psuedotrump and other.suit != self.psuedotrump:
            return True
        if self.suit != self.psuedotrump and other.suit == self.psuedotrump:
            return False
        if self.suit == self.psuedotrump and other.suit == self.psuedotrump:
            if self.value < other.value:
                return False
            else:
                return True
        else: return False
    
    def update(self, trump, psuedo, team):
        self.trump = trump
        self.psuedotrump = psuedo
        self.team = team 
    
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

    def deal(self, times=1):
        for i in range(times):
            self.pop(0)



class Player(object):
    def __init__(self, name= None, teamnumber = None):
        self.name = name
        self.teamnumber = teamnumber
        self.cards = []

    def __repr__(self):
        name = self.name
        return name


class deal(object):
    def __init__(self, list_of_players):
        self.deck = StandardDeck()
        self.list_of_players = list_of_players
        self.list_of_players_cycle = cycle(self.list_of_players)
        self.starting_player = 0
    def deal(self):
        self.deck.shuffle()
        round = 0
        while round < 6:
            start = 0
            i = self.starting_player
            starting_player = self.list_of_players[self.starting_player]
            for player in self.list_of_players_cycle:
                if player == starting_player and start == 0:
                    start = 1
                    self.list_of_players[i%4].cards.append(self.deck.pop())
                    i += 1
                elif player == starting_player and start == 1:
                    break
                elif start == 1:
                    self.list_of_players[i%4].cards.append(self.deck.pop())
                    i += 1
                else:
                    pass        
            round += 1

class game(object):
    def __init__(self):
        self.players = []
        self.players_cycle = cycle(self.players)
        self.team1score = 0
        self.team2score = 0
        self.rounds = 0
        self.wincondition = 11

    def addplayers(self):
        numplayers = 4
        i = 1
        while numplayers > 0:
            Name = input("Enter Player {i}'s name: ".format(i = i))
            self.players.append(Player(name = Name))
            i += 1
            numplayers -=1
        
        randomteam = (input("Want Random Teams?: "))
        if randomteam in ["Yeah", "Yes", "yes", "yeah", "Y", 'y']:
            random.shuffle(self.players)
        print(self.players)
    
    def play(self):
        self.addplayers()
        self.wincondition = int(input("What Would You Like to play till: "))
        hands = deal(self.players)
        hands.deal()
        print(hands.list_of_players[0].cards)
    def bid(self, startingplayer):
        i = 0
        bid = 0
        bidder = None
        while i < 4:
            playerbid = int(input("What is {i}'s bid: ".format(i = self.players[startingplayer%4])))
            if playerbid > bid:
                bid = playerbid
                bidder = self.players[i%4]
            i += 1
            startingplayer += 1
        trump = input("team {x} won the bid, {y} select the trump suit.".format(x = bidder.teamnumber, y = bidder.name ))
    def rounds(self, bidder, trump):
        team1pile = []
        team2pile = []
        pile = []
        starting_player = bidder
        while round < 6:
            start = 0
            for player in self.list_of_players_cycle:
                if player == starting_player and start == 0:
                    start = 1
                    print("Here are your cards, {y}: {Cards}".format(y = player.name, Cards = player.cards))
                    card = input("{y}, please play your card: ".format(y = player.name ))
                    pile.append((player.cards.remove(card), player.teamnumber))
                elif player == starting_player and start == 1:
                    start = 0
                    break
                elif start == 1:
                    self.list_of_players[i%4].cards.append(self.deck.pop())
                    i += 1
                else:
                    pass        
            round += 1
if __name__ == "__main__":
    
    mygame = game()
    mygame.players = [Player(name = "Bob",teamnumber = 1), Player(name = "Hi", teamnumber = 2), Player(name = "Henry", teamnumber = 1), Player(name = "June", teamnumber = 2)]
    #mygame.bid(1)
    print(Card(5, 0, 2, 1).psuedotrump)
    print(Card(5, 1, 2, 1).psuedotrump)
    print(Card(5, 1, 2, 1).suit)
    print(Card(5, 0, 2, 1).suit)