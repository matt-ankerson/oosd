import unittest
from us_address import UsAddress


class TestUsAddress(unittest.TestCase):

    def setUp(self):
        self.good_address = UsAddress("Nigel", "42 Wallaby Way", "Sydney", "NS", "123456789", "Apple", "Sydney")
        self.bad_address = UsAddress(2, 3, 4, 5, 6)

    def test_address_okay(self):
        self.assertTrue(self.good_address.validate_address())
        self.assertFalse(self.bad_address.validate_address())

    def test_repr(self):
        test_address = "Nigel\nApple\n42 Wallaby Way\nSydney\nSydney\nNS\n123456789"
        self.assertEqual(self.good_address.__repr__(), test_address)

# provides a command-line interface to the test script
if __name__ == '__main__':
    unittest.main()