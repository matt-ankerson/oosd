import unittest
from doc_factory import DocumentFactory

# Author: Matt Ankerson
# Date: 12 May 2015


class DocTests(unittest.TestCase):

    def setUp(self):
        self.jsonDict = DocumentFactory.create_document('academic_year.json').doc
        self.xmlDict = DocumentFactory.create_document('academic_year.xml').doc

    def test_dicts_equal(self):
        self.assertDictEqual(self.jsonDict, self.xmlDict)

if __name__ == '__main__':
    unittest.main()