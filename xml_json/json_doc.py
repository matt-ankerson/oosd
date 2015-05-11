from document import Document
import json
from collections import OrderedDict # <-- subslass of Dictionary, remembers the order elements are added

# Author: Matt Ankerson
# Date: 7 May 2015


class JsonDoc(Document):

    def __init__(self, file_path):
        Document.__init__(self)
        self.file_path = file_path
        self.doc = self.read()

    def read(self):
        with open(self.file_path) as raw_json:
            json_str = raw_json.read()
        return json.loads(json_str)
