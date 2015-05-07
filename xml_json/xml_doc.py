from document import Document
import xml.etree.ElementTree as ET

# Author: Matt Ankerson
# Date: 7 May 2015


class XmlDoc(Document):

    def __init__(self, file_path):
        Document.__init__(self)
        self.file_path = file_path
        self.doc = self.read()

    def read(self):
        xml_doc = {}
        return xml_doc