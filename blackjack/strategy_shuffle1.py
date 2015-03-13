import strategy_shuffle
import random

# Author: Matthew Ankerson
# Date: 13 March 2015
# This class serves as a single strategy for shuffling


class StrategyShuffle1(strategy_shuffle.StrategyShuffle):

    def __init__(self):
        strategy_shuffle.StrategyShuffle.__init__(self)

    def shuffle(self, cards):
        random.shuffle(cards)
