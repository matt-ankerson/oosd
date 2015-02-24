# Card class
# Author: Matthew Ankerson
# Date: 23 Feb 2015
# Holds information relevant to a single Card in a Deck.


class Card():
    suits = frozenset("CDHS")
    values = frozenset(range(1, 11) + list("KQJA"))

    # Default constructor
    def __init__(self, value, suit):
        if(suit in self.suits and value in self.values):
            self.suit = suit
            self.value = value
        else:
            raise ValueError("Illegal suit or value")

    def __repr__(self):
        return str(self.value) + str(self.suit)