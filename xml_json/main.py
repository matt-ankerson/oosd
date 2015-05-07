from doc_factory import DocumentFactory

# Author: Matt Ankerson
# Date: 7 May 2015


def print_dictionary(dictionary, indent="", braces=1):
    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            print '%s%s%s%s' % (indent, braces * '[', key, braces * ']')
            print_dictionary(value, indent + '  ', braces + 1)
        else:
            print indent + "%s = %s" % (key, value) + '\n'

if __name__ == "__main__":
    # get the file name/path
    file_name = raw_input("Filename: ")

    # create the document factory
    df = DocumentFactory()

    # create the appropriate document
    doc = df.create_document(file_name)

    # get the dictionary representation from the document
    dic = doc.doc

    # print the dictionary
    print_dictionary(dic)
