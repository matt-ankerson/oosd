from document import Document
import json

# Author: Matt Ankerson
# Date: 18 March 2015


class JsonDocument(Document):

    def __init__(self):
        Document.__init__(self)

    def dump(self, dictionary):
        with open("json_file.json", "w") as out_file:
            json.dump(dictionary, out_file, indent=4)