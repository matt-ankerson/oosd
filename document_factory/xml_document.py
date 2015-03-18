from document import Document
import xml

# Author: Matt Ankerson
# Date: 18 March 2015


class XmlDocument(Document):

    def __init__(self):
        Document.__init__(self)

    # iterate over a list of items, generate appropriate xml
    def get_items(self, items, parent_name):
        output = ""

        for i in items:
            output += "\n<" + parent_name + "_Item>"
            output += "\n" + i
            output += "\n</" + parent_name + "_Item>"

        return output

    # convert the given dictionary to xml
    def convert_to_xml(self, dictionary):

        output = ""
        # iterate over the dictionary
        for key, value in dictionary.items():
            output += "\n<" + key + ">"

            if isinstance(value, list):
                output += self.get_items(value, key)
            elif isinstance(value, dict):
                # use recursion to deal with a nested dictionary
                output += self.convert_to_xml(value)
            else:
                output += "\n   " + value

            output += "\n</" + key + ">"

        return output

    def dump(self, dictionary):
        with open("xml_file.xml", "w") as out_file:
            out_file.write(self.convert_to_xml(dictionary))
            out_file.close()