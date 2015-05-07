from xml_doc import XmlDoc
from json_doc import JsonDoc

# Author: Matt Ankerson
# Date: 7 May 2015


class DocumentFactory():

    def __init__(self):
        pass

    # pass in the file path, create the appropriate dictionary document
    def create_document(self, file_path):
        file_type = file_path.split('.')[1]
        if file_type == "xml":
            return XmlDoc(file_path)
        elif file_type == "json":
            return JsonDoc(file_path)
        else:
            return None