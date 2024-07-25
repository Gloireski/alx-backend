#!/usr/bin/env python3
""" define LRUcache class """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    inherits from BaseCaching class
    overloads def __init__(self)
    """
    def __init__(self):
        """ """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        . Must assign to the dictionary self.cache_data the item
        value for the key key
        . If key or item is None, this method should not do anything.
        . If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            - discard the least recently used item (LRU algorithm)
            - print DISCARD: with the key discarded and following
            by a new line
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # self.cache_data.popitem(last = False) del withou ret
                lru = list(self.cache_data)[0]
                self.cache_data.pop(lru)
                print("DISCARD: {}".format(lru))

    def get(self, key):
        """
        . Must return the value in self.cache_data linked to key.
        . If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        # move the most recently used key to the end
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
