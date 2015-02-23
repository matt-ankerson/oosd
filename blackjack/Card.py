# Card class
# Author: Matthew Ankerson
# Date: 23 Feb 2015
# Holds information relevant to a single Card in a Deck.


class Card():
    suit = None
    value = None

    # Default constructor
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def card(self, suit, value):
        self.suit = suit
        self.value = value