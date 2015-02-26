# Custom error exception raised by oops()

# The try/catch block handles an IndexError, because we have modified MyError to
# inherit IndexError, rather than Exception

# Custom Error class
class MyError(IndexError):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


# Raise MyError
def oops():
    raise MyError(" Value")


try:
    oops()
except IndexError:
    print "Yes, this was an index error"
except MyError as e:
    print "Yes, this was an error of type MyError:" + MyError.__str__(e)
finally:
    print "We're done."





