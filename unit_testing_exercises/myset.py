class MySet:

    def __init__(self, items):
        """Takes a list of items and builds a set with them, removing
           duplicates if necessary.
        """
        self.items = items
        self.items2 = []

        # loop over the list of given items
        for self.x in self.items:
            if self.x not in self.items2:
                self.items2.append(self.x)

        self.items = self.items2

    def add_item(self, item):
        """ Adds an item to the set if it is not already present. If the
            item is present, do nothing.
        """
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item):
        """ Removes item from the set.  Does nothing if item is not
            in the set.
        """
        if item in self.items:
            self.items.remove(item)

    def is_empty(self):
        """Returns True is the set has no members."""
        if len(self.items) == 0:
            return True
        else:
            return False

    def has_item(self, item):
        """returns True if item is in the set, False otherwise."""
        if item in self.items:
            return True
        else:
            return False

    def intersection(self, otherset):
        """Returns a new set that is the intersection of self
           and otherset.
           """
        # return self.intersection(otherset)
        intersect = [x for x in otherset if x in self.items]
        return intersect


    def union(self, otherset):
        """"Returns a new set that is the union of self and otherset"""
        # append all values from 'a' to 'b', to make a new set 'c'
        union = [x for x in otherset + self.items]
        return union

    def is_subset_of(self, otherset):
        """Returns True if self is a subset of otherset."""
        # This method doesn't require the subset values to exist consecutively.
        subset = [x for x in otherset if x in self.items]
        return len(subset) == len(self.items)
        # return otherset.__contains__(self.items)
        # return set(self.items) < set(otherset)

    def is_equal_to(self, otherset):
        """Returns True if self and otherset are equal, i.e.,
           they have the exact same members.
        """
        return self.items == otherset

    def is_proper_subset_of(self, otherset):
        """Returns True is self is a *proper* subset of otherset."""
        # "A proper subset is a subset that has at least one less element than it's super set."
        subset = [x for x in otherset if x in self.items]
        return len(subset) < (len(otherset) - 1)
