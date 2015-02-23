import Card
import random

# Deck class
# Author: Matthew Ankerson
# Date: 24 Feb 2015
# This class holds cards and performs functions necessary for a Deck


class Deck():
    cards = None

    # Default constructor
    # Create the Deck of Cards
    def __init__(self):
        cards = []
        for suit in ['C', 'D', 'H', 'S']:
            for value in range(1, 11):
                self.cards.append(Card.Card(value, suit))
            for value in ['J', 'Q', 'K', 'A']:
                self.cards.append(Card.Card(value, suit))
        random.shuffle(self.cards)

    # Remove and return a given card from the list of cards
    def getCard(self):
        return self.cards.pop()
