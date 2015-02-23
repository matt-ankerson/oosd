import Card
# Deck class
# Author: Matthew Ankerson
# Date: 23 Feb 2015
# This class holds cards and performs functions necessary for a Deck


class Deck():
    cards = None

    # Default constructor
    # Create the Deck of Cards
    #def __init__(self):

    # Create a complete deck of Cards
    def makecards(self):
        # Loop over the 52 Cards
        for i in xrange(52):
            c = Card.Card(1, (i + 1))     # Create a new Card