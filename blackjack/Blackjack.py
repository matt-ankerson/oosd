#! /usr/bin/python

# Blackjack Game
# Author: Matt Ankerson
# Adapted from Tom Clark's version

import sys
import Deck
import Participant
import House

d = Deck.Deck()
p = Participant.Participant()
h = House.House()

# Deal two cards to each participant
p.takeCard(d.getCard())
h.takeCard(d.getCard())
p.takeCard(d.getCard())
h.takeCard(d.getCard())

# Show the hands, keep one of the dealer's cards hidden
print("House: " + h.showHandHiddenDown())
print("You: " + p.showHand())

print("Your play")

# p.hitOrStand will return true while the player wants to hit
while(p.hitOrStand(h.hand, d)):
    p.takeCard(d.getCard())
    print("House: " + h.showHandHiddenDown())
    print("You " + p.showHand())
    print("==========")
    print("")

print("")
print("House's play:")
print("House: " + h.showHand())
print("You: " + p.showHand())
print("==========")
print("")
# h.hitOrStand will return true or false
while(h.hitOrStand(p.hand, d)):
    h.takeCard(d.getCard())
    print("House: " + h.showHand())
    print("You: " + p.showHand())
    print("==========")
    print("")
    if(h.getScore() > 21):
        print("Busted!")
        sys.exit()
    print("")

if p.getScore() > h.getScore() & p.getScore() <= 21:
    print("You win!")
else:
    print("House wins")







