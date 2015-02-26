import Hand


# BlackjackHand class
# Date: 26 Feb 2015
# Holds and manages the cards in a hand for a participant (in a game of Blackjack)

# This class was created in order to resolve the Open/Closed Principle violation
# presented by the Hand class

# I decided that a "Hand" class should be usable in almost every card game implementation.
# By separating the "Blackjack" specific functionality I removed the danger of having to modify
# the "Hand" class to suit future implementations.

class BlackjackHand(Hand.Hand):

    # Calculate and return the score of this BlackjackHand
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