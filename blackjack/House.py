import Participant
import re

# House class
# Date: 24 Feb 2015
# This class inherits Participant class and adds methods relevant only to the House


class House(Participant.Participant):

    # Offer another implementation of hitOrStand()
    # Stand if the score is above 17
    def hitOrStand(self):
        return self.hand.getScore() < 17

    # Show the flop
    def showHandHiddenDown(self):
        cards = str(self.hand)

        # Replace the first card with **
        # Regular expression .compile
        cardToHide = re.compile("(^\w+)\s")
        return cardToHide.sub("** ", cards)