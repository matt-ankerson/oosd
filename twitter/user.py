# Author: Matt Ankerson
# Date: 27 March 2015
# This class can act as a subject and an observer


class User():

    def __init__(self):
        self.observers = []
        self.subject = None
        self.send_tweet = ""
        self.receive_tweet = ""

    # set the subject, and add myself to the subject's list of observers.
    def set_subject(self, subject):
        self.subject = subject
        # call subject's add_observer method, passing in self.
        subject.add_observer(self)

    # add an observer to the list of observers
    def add_observer(self, o):
        self.observers.append(o)

    # remove an observer from the list of observers
    def remove_observer(self, o):
        self.observers.remove(o)

    # update all observers, call each of their update() methods
    def notify_observers(self):
        for o in self.observers:
            o.update(self.send_tweet)

    # set send_tweet to the new message
    def _set_send_tweet(self, new_tweet):
        self.__dict__["send_tweet"] = new_tweet
        self.notify_observers()

    # interrupt the setting of our send_tweet variable
    def __setattr__(self, key, value):
        if key == "send_tweet":
            self._set_send_tweet(value)
        else:
            self.__dict__[key] = value

    # subject will call this when a new tweet is received
    def update(self, new_tweet):
        self.receive_tweet = new_tweet
