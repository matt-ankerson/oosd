from document import Document

# Author: Matt Ankerson
# Date: 7 May 2015


class JsonDoc(Document):

    def __init__(self, file_path):
        Document.__init__(self)
        self.file_path = file_path
        self.doc = self.read()

    def read(self):
        json_doc = {}
        return json_doc