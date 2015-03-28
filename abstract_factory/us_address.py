from abstract_address_factory import AddressFactory

# Author: Matt Ankerson
# Date: 24 March 2015
# This class validates its data and prints its data in the correct format


class UsAddress(AddressFactory):

    # Accept all params necessary for a UK address, allow for optional fields using optional params
    def __init__(self, recipient, address_line_1, city, state, post_code, organisation="", address_line_2=""):
        self.recipient = recipient
        self.address_line_1 = address_line_1
        self.city = city
        self.state = state
        self.post_code = post_code
        self.organisation = organisation
        self.address_line_2 = address_line_2

    def validate_address(self):
        address_okay = True
        # ensure that all data is of the appropriate type
        if not isinstance(self.recipient, str) or not isinstance(self.address_line_1, str)\
                or not isinstance(self.city, str) or not isinstance(self.state, str)\
                or not isinstance(self.organisation, str) or not isinstance(self.post_code, str)\
                or not isinstance(self.address_line_2, str):
            address_okay = False
        return address_okay

    # string the data together in the correct format and return it
    def __repr__(self):
        address = ""
        address += self.recipient + "\n"
        if not self.organisation == "":
            address += self.organisation + "\n"
        address += self.address_line_1 + "\n"
        if not self.address_line_2 == "":
            address += self.address_line_2 + "\n"
        address += self.city + "\n"
        address += self.state + "\n"
        address += self.post_code

        return address