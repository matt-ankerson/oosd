import strategy_hits

""" this class implements one strategy that we can plug into The Player class """
# Author: Matthew Ankerson
# Date: 12 March 2015

class Strategy1(strategy_hits.Strategy):

    def __init__(self):
        strategy_hits.Strategy.__init__(self)

    # implements a unique strategy - require user input.
    # Simply allow the user to cheat by looking at the house's hand.
    def hit_or_stand(self, own_hand, other_hand, deck):
        # show the user something they should consider in their decision.
        print("The house's hand: " + other_hand.__repr__())
        return raw_input("(h)it or (s)tand: ") == "h"