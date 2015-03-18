from xml_document import XmlDocument
from yaml_document import YamlDocument
from json_document import JsonDocument
from random import Random

# Author: Matt Ankerson
# Date: 18 March 2015


class DocumentFactory():

    def __init__(self):
        self.rand = Random()

    def create_document(self, desired_type):
        if desired_type == "xml":
            return XmlDocument()
        elif desired_type == "yaml":
            return YamlDocument()
        elif desired_type == "json":
            return JsonDocument()
        else:
            return None

    def create_random_document(self):
        selector = self.rand.randint(0, 2)
        if selector == 0:
            return XmlDocument()
        elif selector == 1:
            return YamlDocument()
        elif selector == 2:
            return JsonDocument()
        else:
            return None