import unittest
from uk_address import UkAddress


class TestUkAddress(unittest.TestCase):

    def setUp(self):
        self.good_address = UkAddress("Nigel", "42 Wallaby Way", "Sydney", "SO31 4NG", "Apple", "Big Ben", "Local")
        self.bad_address = UkAddress(2, 3, 4, 5, 6)

    def test_address_okay(self):
        self.assertTrue(self.good_address.validate_address())
        self.assertFalse(self.bad_address.validate_address())

    def test_repr(self):
        test_address = "Nigel\nApple\nBig Ben\n42 Wallaby Way\nLocal\nSydney\nSO31 4NG"
        self.assertEqual(self.good_address.__repr__(), test_address)

# provides a command-line interface to the test script
if __name__ == '__main__':
    unittest.main()
