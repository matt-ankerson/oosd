from abstract_phone_factory import PhoneFactory

# Author: Matt Ankerson
# Date: 24 March 2015
# This class validates its data and prints its data in the correct format


class UsPhone(PhoneFactory):

    def __init__(self, area_code, prefix, number):
        self.area_code = area_code
        self.prefix = prefix
        self.number = number

    # validate our given phone number data
    def validate_phone_number(self):
        phone_okay = True
        if len(self.area_code) != 3:
            phone_okay = False
        if len(self.prefix) != 3:
            phone_okay = False
        if len(self.number) != 4:
            phone_okay = false
        return phone_okay

    def __repr__(self):
        # Print in appropriate format
        us_number = str(self.area_code) + "-"
        us_number += str(self.prefix) + "-"
        us_number += str(self.number)
        return us_number

