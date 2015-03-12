import Participant
import strategy2
import re

# House class
# Date: 24 Feb 2015
# This class inherits Participant class and adds methods relevant only to the House

class House(Participant.Participant):

    def __init__(self):
        self.strat2 = strategy2.Strategy2()
        Participant.Participant.__init__(self)

    # Use the strategy from strategy2
    def hitOrStand(self, other_hand, deck):
        return self.strat2.hit_or_stand(self.hand, other_hand, deck)

    # Show the flop
    def showHandHiddenDown(self):
        cards = str(self.hand)

        # Replace the first card with **
        # Regular expression .compile
        cardToHide = re.compile("(^\w+)\s")
        return cardToHide.sub("** ", cards)