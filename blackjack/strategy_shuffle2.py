import strategy_shuffle
import random

# Author: Matthew Ankerson
# Date: 13 March 2015
# This class serves as a single strategy for shuffling


class StrategyShuffle2(strategy_shuffle.StrategyShuffle):

    def __init__(self):
        strategy_shuffle.StrategyShuffle.__init__(self)

    # Exchange each card in the deck with one at a randomly selected index
    def shuffle(self, cards):
        for i in xrange(0, len(cards)):
            temp = cards[i]
            other_card_index = random.randint(0, len(cards) - 1)
            cards[i] = cards[other_card_index]
            cards[other_card_index] = temp
