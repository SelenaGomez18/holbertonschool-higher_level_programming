#!/usr/bin/env python3
"""CountedIterator class - keeps track of how many items have been iterated."""


class CountedIterator:
    """An iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter set to 0."""
        self.iterator = iter(iterable)
        self.count = 0
    def __next__ (self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated."""
        return self.count

    def __iter__(self):
        """Return the iterator itself (for use in for loops)."""
        return self
