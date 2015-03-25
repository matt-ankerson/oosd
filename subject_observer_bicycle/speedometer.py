# Author: Matt Ankerson
# Date: 25 March 2015
# Determines speed from RPM


class Speedometer():

    def __init__(self, subject):
        self.speed = 0
        # save reference to subject.
        self.subject = subject
        # call subject's add_observer method, passing in self.
        subject.add_observer(self)

    # subject will call this when rpms change
    def update(self, rpms):
        self.speed = 205 * (60 * rpms)/100000.0