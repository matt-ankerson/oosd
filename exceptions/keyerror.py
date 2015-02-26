# KeyError exception raised by oops()
# while the try/catch will only catch an IndexError

# This produces an exception type error

def oops():
    raise KeyError()


try:
    oops()
except IndexError:
    print "Yes, this was an index error"
finally:
    print "We're done."
