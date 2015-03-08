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

    def test_union(self):
        testunion = [1, 2, 3, 4, 5, 6, 7]
        testinput = [6, 7]
        self.assertItemsEqual(self.myset.union(testinput), testunion)

    def test_is_subset(self):
        testsubset = [1, 2, 3, 4, 5, 6]
        self.assertTrue(self.myset.is_subset_of(testsubset))
        self.assertFalse(self.myset.is_subset_of([9, 8, 7]))

    def test_is_equal_to(self):
        test_equal_set = [1, 2, 3, 4, 5]
        self.assertTrue(self.myset.is_equal_to(test_equal_set))
        self.assertFalse(self.myset.is_equal_to([1, 2, 3]))

    def test_is_proper_subset(self):
        testbigsuperset = [1, 2, 3, 4, 5, 6, 7]
        testsmallsuperset = [1, 2, 3, 4]
        self.assertTrue(self.myset.is_proper_subset_of(testbigsuperset))
        self.assertFalse(self.myset.is_proper_subset_of(testsmallsuperset))

if __name__ == '__main__':
    unittest.main()
