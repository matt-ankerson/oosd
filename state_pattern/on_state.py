from light_state import LightState
import off_state

# Author: Matt Ankerson
# Date: 1 April 2015


class OnState(LightState):

    def switch(self):
        # change state to 'off'.
        return off_state.OffState()

    def __repr__(self):
        return "The light is on."
