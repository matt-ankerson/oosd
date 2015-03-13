import Card

# Deck class
# Author: Matthew Ankerson
# Date: 24 Feb 2015
# This class holds cards and performs functions necessary for a Deck


class Deck():

    # Default constructor
    # Create the Deck of Cards
    def __init__(self, strategy):
        self.cards = []
        self.strategy = strategy
        for suit in "CDHS":
            for value in range(1, 11):
                self.cards.append(Card.Card(value, suit))
            for value in "AKQJ":
                self.cards.append(Card.Card(value, suit))

        # shuffle the cards. implement strategy pattern here.
        # random.shuffle(self.cards)
        strategy.shuffle(self.cards)

    # Remove and return a given card from the list of cards
    def getCard(self):
        return self.cards.pop()

    # Return a string representation of this Deck
    def __repr__(self):
        deck_string = ""
        for c in self.cards:
            deck_string += str(c)
            deck_string += " "
        return deck_string
