import unittest
import Deck
import strategy_shuffle1
import strategy_shuffle2

# Author: Matt Ankerson
# Date: 13 March 2015


class TestStrategyShuffle(unittest.TestCase):

    def setUp(self):
        # create two decks and a strategy for each.
        self.strat_shuffle1 = strategy_shuffle1.StrategyShuffle1()
        self.strat_shuffle2 = strategy_shuffle2.StrategyShuffle2()
        self.deck_shuffle1 = Deck.Deck(self.strat_shuffle1)
        self.deck_shuffle2 = Deck.Deck(self.strat_shuffle2)

    def test_shuffle1(self):
        # Create a new deck, but don't shuffle it
        fresh_deck = Deck.Deck(self.strat_shuffle1)
        self.deck_shuffle1.strategy.shuffle(self.deck_shuffle1.cards)
        self.assertNotEquals(fresh_deck, self.deck_shuffle1)

    def test_shuffle2(self):
        # Create a new deck, but don't shuffle it
        fresh_deck = Deck.Deck(self.strat_shuffle2)
        self.deck_shuffle2.strategy.shuffle(self.deck_shuffle2.cards)
        self.assertNotEquals(fresh_deck, self.deck_shuffle1)
