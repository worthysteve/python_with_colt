from random import shuffle
# Deck of Cards Exercise Introduction Text
# OOP Exercise
# Introduction

# Your goal in this exercise is to implement two classes, Card  and Deck .

# Specifications

#! Card 

class Card:
    def __init__(self, value, suit):
       self.value = value 
       self.suit = suit 
    
    #* Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
    def __repr__(self):
        # return "{} of {}".format(self.value, self.suit)
        return f"{self.value} of {self.suit}"

#* Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").

#* Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").

# c = Card("A", "Hearts")
# c2 = Card("10", "Diamonds")
# c3 = Card("K", "Spades")

# print(c, c2, c3);

#! Deck 
class Deck:
    def __init__(self):

        #* Each instance of Deck  should have a cards attribute with all 52 possible instances of Card.
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # self.cards = []
        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        # print(self.cards);

        # list comprehension
        self.cards = [Card(value, suit) for suit in suits for value in values]
        print(self.cards);
    
    #* Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    #* Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
    def count(self):
        return len(self.cards)
    
    #* Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    

    #* Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
    def deal_card(self):
        return self._deal(1)[0]
    
    #* Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.
    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    #* Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

# d = Deck()
# # d.cards.pop()
# # print(d.count());
# # print(d);
# # print(d._deal(52));
# # print(d.count());
# # print(d._deal(3));

# d.shuffle()
# print(d.cards);

# Test the shuffle method
d = Deck()
# print("Original deck:")
# print(d.cards)

d.shuffle()
print("\nShuffled deck:")
print(d.cards)
card  = d.deal_card()
print(card);
hand = d.deal_hand(50)
card2  = d.deal_card()
print(card2);
# print(hand);
card2  = d.deal_card()
print(d.cards);