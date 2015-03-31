# Author: Matt Ankerson
# Date: 1 April 2015
# This is the parent state object. Our various states descend from this.


class LightState(object):

    # the 'respond()' method
    def switch(self):
        raise NotImplementedError("")
