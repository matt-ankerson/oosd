from document_factory import DocumentFactory

# Author: Matt Ankerson
# Date: 18 March 2015


def construct_dictionary():
    dictionary = {'name': 'matt', 'role': 'student', 'hobbies': ['farming', 'programming', 'kayaking'],
            'favourite_beer': {'brewer': 'speights', 'beer': 'gold_medal_ale'}}
    return dictionary;

# Create the DocumentFactory
df = DocumentFactory()

# Get a Dictionary
test_dict = construct_dictionary()

# Get a document from the DocumentFactory
doc = df.create_document("yaml")

# Try export dictionary to a file
doc.dump(test_dict)
