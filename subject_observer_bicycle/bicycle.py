# Author: Matt Ankerson
# Date: 25 March 2015
# This class is the subject in the subject-observer pattern
# Keeps track of RPM


class Bicycle():

    def __init__(self):
        self.observers = []
        self.current_rpms = 0

    # append to list of observers
    def add_observer(self, observer):
        self.observers.append(observer)

    # remove from list of observers
    def remove_observer(self, observer):
        self.observers.remove(observer)

    # iterate over observers, call each of their update() methods
    def notify_observers(self):
        for o in self.observers:
            o.update(self.current_rpms)

    # set the current rpms
    def _set_rpms(self, rpms):
        self.__dict__["current_rpms"] = rpms
        self.notify_observers()

    def __setattr__(self, key, value):
        if key == "current_rpms":
            self._set_rpms(value)
        else:
            self.__dict__[key] = value