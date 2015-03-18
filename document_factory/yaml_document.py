from document import Document
import pyaml

# Author: Matt Ankerson
# Date: 18 March 2015


class YamlDocument(Document):

    def __init__(self):
        Document.__init__(self)

    def dump(self, dictionary):
        with open("yaml_file.yaml", 'w') as open_file:
            open_file.write(pyaml.dump(dictionary))
            open_file.close()