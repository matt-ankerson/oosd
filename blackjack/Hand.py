import Deck

# Hand class
# Date: 24 Feb 2015
# Holds and manages the cards in a hand for a participant

# Does the Hand class violate the Open/Closed Principle?
# That is that it should be open for extension but closed for modification.

class Hand():
    #cards = None

    def __init__(self):
        self.cards = []

    # Add a card to our list of cards in this Hand
    def addCard(self, card):
        self.cards.append(card)

    # Return the number of cards in this hand
    def getSize(self):
        return len(self.cards)

    # Calculate and return the score of this Hand
    def getScore(self):
        # Separate the aces from normal cards
        regular_cards = [c for c in self.cards if c.value != "A"]
        aces = [c for c in self.cards if c.value == "A"]

        # Add up regular card values:
        points = 0
        # Loop over the regular cards
        for c in regular_cards:
            if isinstance(c.value, basestring):
                points += 10
            else:
                points += c.value
        # Add ace values
        for c in aces:
            if points + 11 <= 21:
                points += 11
            else:
                points += 1

        return points

    # Return a string representation of this Hand
    def __repr__(self):
        hand_string = ""
        for c in self.cards:
            hand_string += str(c)
            hand_string += " "
        return hand_string




























































































































