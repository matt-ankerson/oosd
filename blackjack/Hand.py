import Deck

# Hand class
# Date: 24 Feb 2015
# Holds and manages the cards in a hand for a participant

# Does the Hand class violate the Open/Closed Principle?
# That is that it should be open for extension but closed for modification.

class Hand():
    cards = None

    def __init__(self):
        self.cards = []

    # Add a card to our list of cards in this Hand
    def addCard(self, card):
        self.cards.append(card)

    # Return the number of cards in this hand
    def getSize(self):
        return len(self.cards)

    # getScore method has been removed from the Hand class and placed in the
    # child class (BlackjackHand)

    # Return a string representation of this Hand
    def __repr__(self):
        hand_string = ""
        for c in self.cards:
            hand_string += str(c)
            hand_string += " "
        return hand_string




























































































































