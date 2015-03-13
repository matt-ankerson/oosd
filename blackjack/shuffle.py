import Deck
import strategy_shuffle1
import strategy_shuffle2

# Author: Matt Ankerson
# Date: 13 March 2015
# This file tests the shuffle strategies


# create two decks with a strategy for each. The decks will shuffle themselves
strat_shuffle1 = strategy_shuffle1.StrategyShuffle1()
strat_shuffle2 = strategy_shuffle2.StrategyShuffle2()
deck_shuffle1 = Deck.Deck(strat_shuffle1)
deck_shuffle2 = Deck.Deck(strat_shuffle2)

# print out the decks
print("Deck 1 - using Strategy 1.\r")
print(deck_shuffle1.__repr__())
print("")
print("Deck 2 - using Strategy 2.\r")
print(deck_shuffle2.__repr__())

# * Test the effectiveness of each shuffle method *
# To record the results - employ a Python dictionary using the card values as keys.
# For the dictionary values, use lists which show the positions (0-51) that a card
# occupies in a shuffled deck.

# set up the dictionary.
dictionary = {}

for card in deck_shuffle1.cards:
    positions = [0] * 52
    dictionary[card.__repr__()] = positions

# iterate 520 times
for i in xrange(0, 520):
    # shuffle the deck
    deck_shuffle1.strategy.shuffle(deck_shuffle1.cards)

    # iterate over the deck
    for card_index in xrange(0, len(deck_shuffle1.cards)):
        cardValue = deck_shuffle1.cards[card_index].__repr__()
        # increment the appropriate value in the dictionary
        dictionary.get(cardValue)[card_index] += 1

# Determine how successful the shuffle was.

