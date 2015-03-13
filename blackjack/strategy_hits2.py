import strategy_hits

""" this class implements one strategy that we can plug into The Player class """
# Author: Matthew Ankerson
# Date: 12 March 2015

class Strategy2(strategy_hits.Strategy):

    def __init__(self):
        strategy_hits.Strategy.__init__(self)

    # implements a unique strategy - make a decision based on the user's hand.
    # ie. don't hit if the user has already bust.
    def hit_or_stand(self, own_hand, other_hand, deck):
        if other_hand.getScore() > 21:
            return False
        else:
            return True
