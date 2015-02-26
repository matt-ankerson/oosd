# IndexError exceptions

def oops():
    raise IndexError()


try:
    oops()
except IndexError:
    print "Yes, this was an index error"
finally:
    print "We're done."
