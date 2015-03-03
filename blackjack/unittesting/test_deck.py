import unittest
import Card


class TestCardClass(unittest.TestCase):

    def setUp(self):
        self.okaySuits = frozenset("CDHS")
        self.okayValues = frozenset(range(1, 11) + list("KQJA"))
        self.card = Card.Card(2, 'C')

    def test_value(self):
        # Ensure that the card is being created with the correct value
        self.assertEqual(self.card.value, 2)

    def test_suit(self):
        # Ensure that the card is being created with the correct suit
        self.assertEqual(self.card.suit, 'C')

    def test_str(self):
        # Ensure that we get our expected string representation
        return_string = "2C"
        self.assertEqual(self.card.__repr__(), return_string)

# provides a command-line interface to the test script
if __name__ == '__main__':
    unittest.main()

