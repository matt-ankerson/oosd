from abstract_address_factory import AddressFactory

# Author: Matt Ankerson
# Date: 24 March 2015
# This class validates its data and prints its data in the correct format


class UkAddress(AddressFactory):

    # Accept all params necessary for a UK address, allow for optional fields using optional params
    def __init__(self, recipient, address_line, city, post_code, organisation="", building_name="", locality=""):
        self.recipient = recipient
        self.address_line = address_line
        self.city = city
        self.post_code = post_code
        self.organisation = organisation
        self.building_name = building_name
        self.locality = locality

    # validate the address data
    def validate_address(self):
        address_okay = True

        # ensure that all data is of the appropriate type
        if not isinstance(self.recipient, str) or not isinstance(self.address_line, str)\
                or not isinstance(self.city, str) or not isinstance(self.post_code, str)\
                or not isinstance(self.organisation, str) or not isinstance(self.building_name, str)\
                or not isinstance(self.locality, str):
            address_okay = False

        return address_okay

    # string the data together in the correct format and return it
    def __repr__(self):
        address = ""
        address += self.recipient + "\n"
        if not self.address_line == "":
            address += self.address_line + "\n"

        return address