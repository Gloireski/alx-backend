#!/usr/bin/env python3
""" define LIFPcache class """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching class
    overloads def __init__(self)
    """
    def __init__(self):
        """ """
        super().__init__()

    def put(self, key, item):
        """
        . Must assign to the dictionary self.cache_data the item
        value for the key key
        . If key or item is None, this method should not do anything.
        . If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            - discard the first item put in cache (FIFO algorithm)
            - print DISCARD: with the key discarded and following
            by a new line
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # print(my_dict.popitem(last=False))
                liKey = list(self.cache_data)[len(self.cache_data) - 2]
                self.cache_data.pop(liKey)
                print("DISCARD: {}".format(liKey))

    def get(self, key):
        """
        . Must return the value in self.cache_data linked to key.
        . If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
