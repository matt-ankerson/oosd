# Card class
# Author: Matthew Ankerson
# Date: 23 Feb 2015
# Holds information relevant to a single Card in a Deck.


class Card():
    suits = list['S', 'D', 'H', 'C']
    values = list[1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 'K', 'Q', 'J', 'A']

    # Default constructor
    def __init__(self, suit, value):
        if(suit in self.suits and value in self.values):
            self.suit = suit
            self.value = value

    def  __repr__(self):
        return str(self.value) + self.suit