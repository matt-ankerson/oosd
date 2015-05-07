from document import Document
import xml.etree.ElementTree as ET

# Author: Matt Ankerson
# Date: 7 May 2015


class XmlDoc(Document):

    def __init__(self, file_path):
        Document.__init__(self)
        self.file_path = file_path
        self.doc = self.read()

    # This function only pulls tags and attributes from xml, not inner text. Need to fix this.
    def tree_to_dict(self, tree):
        # map returns a new list produced by applying the given function to each element in the given list
        dic = {tree.tag: map(self.tree_to_dict, tree.getchildren())}
        dic.update((k, v) for k, v in tree.attrib.iteritems())  # <<-- we also need the inner text.
        return dic

    def read(self):
        tree = ET.parse(self.file_path)
        print(self.file_path)
        xml_doc = self.tree_to_dict(tree.getroot())
        return xml_doc