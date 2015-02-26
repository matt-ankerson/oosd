import BlackjackHand

# Participant class - serves as a parent class to the House class
# Date 24 Feb 2015

class Participant():
    hand = None

    # Constructor
    def __init__(self):
        self.hand = BlackjackHand.BlackjackHand

    # Remove a card from the deck and add to this players hand
    def takeCard(self, card):
        self.hand.addCard(card)

    # Return a string representation of this player's hand
    def showHand(self):
        return str(self.hand) + " Score: " + str(self.hand.getScore())

    # Return a boolean value indicating whether the user wishes to hit or stand
    def hitOrStand(self):
        return (raw_input("(h)it or (s)tand: ") == "h")

    # Return the score of this player's hand
    def getScore(self):
        return self.hand.getScore()
