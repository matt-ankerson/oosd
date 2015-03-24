from abc import ABCMeta, abstractmethod

# Author: Matt Ankerson
# Date: 24 March 2015
# This class is abstract and is never instantiated. Though classes will derive from this.


class PhoneFactory():
    __metaclass__ = ABCMeta

    @abstractmethod
    def validate_phone_number(self):
        pass
