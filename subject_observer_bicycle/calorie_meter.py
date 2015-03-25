# Author: Matt Ankerson
# Date: 25 March 2015
# Determines calories from RPM


class CalorieMeter():

    def __init__(self, subject):
        self.calories = 0
        # save reference to subject.
        self.subject = subject
        # call subject's add_observer method, passing in self.
        subject.add_observer(self)

    # subject will call this when rpms change
    def update(self, rpms):
        self.calories = rpms * 5
