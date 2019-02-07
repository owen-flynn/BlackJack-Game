import random

class Deck:
    def __init__(self):
        self.cards = []

    def build_deck(self,card):
        vals = range(1,14)
        suits = ["Spades","Clubs","Hearts","Diamonds"]
        self.cards = [card(rank = val, suit = suit ) for val in vals for suit in suits]

    def shuffle(self):
        for i in range(len(self.cards)-1, 1, -1):
            rand = random.randrange(i)
            t = self.cards[i]
            self.cards[i] = self.cards[rand]
            self.cards[rand] = t
        
    def show_deck(self):
        for card in self.cards:
            print(card.rank)
            print(card.suit)

class Hand:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
        self.cards = []
        self.score = 0

    def reset(self):
        self.cards = []
        self.score = 0

    def deal(self,deck):
        self.cards.append(deck.cards.pop())
        self.cards.append(deck.cards.pop())

    def hit(self,deck):
        self.cards.append(deck.cards.pop())

    def get_sum(self,cards):
        sum = 0
        val = 0

        for card in cards:
            if(card.rank >= 11 and card.rank <= 13):
                val = 10
            else:
                val = card.rank

            sum = sum + val

        return sum

    def has_ace(self,cards):
        for card in cards:
            if card.rank == 1:
                return True

        return False

    def calculate_score(self):
        total = self.get_sum(self.cards)

        if self.has_ace(self.cards):
            new_total = total + 10
            if(new_total <= 21):
                score = new_total
            else:
                score = total
        else:
            score = total

        self.score = score

    def calculate_initial_dealer_score(self):
        val = self.cards[1].rank
        if val == 1:
            self.score = 11
        elif val >= 11:
            self.score = 10
        else:
            self.score = val

    def show_hand(self):
        for card in self.cards:
            print(card.rank," of ", card.suit)
