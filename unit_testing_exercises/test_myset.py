import unittest
import myset

class TestMySet(unittest.TestCase):

    def setUp(self):
        self.testitems = [1, 2, 3, 4, 5]
        self.myset = myset.MySet(self.testitems)

    def test_add_item(self):
        self.testitems.append(6)
        self.myset.add_item(6)
        self.assertEqual(self.myset.items, self.testitems)

    def test_remove_item(self):
        self.testitems.remove(5)
        self.myset.remove_item(5)
        self.assertEqual(self.testitems, self.myset.items)

    def test_is_empty(self):
        self.assertFalse(self.myset.is_empty())
        self.myset.items = []
        self.assertTrue(self.myset.is_empty())

    def test_has_item(self):
        self.assertTrue(self.myset.has_item(2))
        self.assertFalse(self.myset.has_item(9))

    def test_intersection(self):
        testintersect = [1, 2, 3, 4, 5]
        self.assertEqual(self.myset.intersection(self.testitems), testintersect)

        # assertItemsEqual

if __name__ == '__main__':
    unittest.main()
