import states

# Author: Matt Ankerson
# Date: 14 April 2015

# This class represents the vending machine itself.


class VendingMachine():

    def __init__(self):
        self.state = states.WaitingState()
        self.money_received = 0.00
        self.products = {"Chips": 3.00, "Chocolate": 2.50, "Peanuts": 3.0}
        self.selection = ""

    # Add to the received amount of money
    def insert_money(self, amount):
        self.money_received = self.money_received + amount

    # Refund money and return all to normal
    def cancel_transaction(self):
        self.state = states.MakingChangeState()

    # Decide if a valid selection was given.
    def make_selection(self, selection):
        self.selection = selection

    def change_state(self):
        # delegate implementation to the states
        self.state = self.state.change_state(self)

    # Return a status message, indicating current state.
    def get_status(self):
        return self.state.__repr__()
