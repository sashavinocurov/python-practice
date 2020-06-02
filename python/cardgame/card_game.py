import random

class Card:
    def __init__(self, suite, value, name):
        self.suite = suite
        self.value = value
        self.name = name

class Deck:
    def __init__(self):
        self.deck= []
        for i in range (1,14):
            self.cardHelper("Hearts", i)
        for i in range (1,14):
            self.cardHelper("Diamonds", i)
        for i in range (1,14):
            self.cardHelper("Spades", i)
        for i in range (1,14):
            self.cardHelper("Clubs", i)
        random.shuffle(self.deck)
    
    def cardHelper(self, suit, value):
        if (value == 1):
            self.deckappend(Card(suit,value, "Ace"))
        elif (value == 11):
            self.deckappend(Card(suit,value, "Jack"))
        elif (value == 12):
            self.deckappend(Card(suit,value, "Queen"))
        elif (value == 13):
            self.deckappend(Card(suit,value, "King"))
        else:
            self.deckappend(Card(suit,value, str(value)))
        self        
    def carddraw(self,name):
        self.card = random.choice(deck)
        deck.remove(card)
        suit1, value1= card

print(Card)