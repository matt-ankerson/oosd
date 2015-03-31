from light_state import LightState
from on_state import OnState

# Author: Matt Ankerson
# Date: 1 April 2015


class OffState(LightState):
    
    def switch(self):
        # change state to 'on'.
        return OnState()

    def __repr__(self):
        return "The light is off."