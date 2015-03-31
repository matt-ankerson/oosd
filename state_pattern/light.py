import off_state
import on_state

# Author: Matt Ankerson
# Date: 1 April 2015
# This Light class uses two state objects to represent it's state.


class Light():

    def __init__(self):
        self.state = off_state.OffState()

    def switch(self):
        # delegate implementation to the states
        self.state = self.state.switch()

    def display(self):
        return str(self.state.__repr__())