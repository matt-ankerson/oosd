import Hand
import strategy1

# Participant class - serves as a parent class to the House class
# Date 24 Feb 2015


class Participant():

    # Constructor
    def __init__(self):
        self.hand = Hand.Hand()
        self.strat = strategy1.Strategy1()

    # Remove a card from the deck and add to this players hand
    def takeCard(self, card):
        self.hand.addCard(card)

    # Return a string representation of this player's hand
    def showHand(self):
        return str(self.hand) + " Score: " + str(self.hand.getScore())

    # Return a boolean value indicating whether this participant wishes to hit or stand
    def hitOrStand(self, other_hand, deck):
        return self.strat.hit_or_stand(self.hand, other_hand, deck)

    # Return the score of this player's hand
    def getScore(self):
        return self.hand.getScore()
