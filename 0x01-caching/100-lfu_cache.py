#!/usr/bin/env python3
""" define LRUcache class """
from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    inherits from BaseCaching class
    overloads def __init__(self)
    __stats (list): A dictionary of cache keys for access count
    __rlock (RLock): Lock accessed resources to prevent race condition
    """
    def __init__(self):
        """ """
        super().__init__()
        # self.cache_data = OrderedDict()
        # self.cache_count = {}
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """
        . Must assign to the dictionary self.cache_data the item
        value for the key key
        . If key or item is None, this method should not do anything.
        . If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            - discard the least frequency used item (LRU algorithm)
            -if you find more than 1 item to discard, you must use
            the LRU algorithm to discard only the least recently used
            - print DISCARD: with the key discarded and following
            by a new line
        """
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_count[key] = 0
            # print(self.cache_count[key])
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                v = list(self.cache_count.values())
                k = list(self.cache_count.keys())
                mn = min(v)
                if v.count(mn) > 1:
                    lru = list(self.cache_data)[0]
                    self.cache_data.pop(lru)
                    self.cache_count.pop(lru)
                    print("DISCARD lru: {}".format(lru))
                else:
                    lfu = k[v.index(mn)]
                    self.cache_data.pop(lfu)
                    self.cache_count.pop(lfu)
                    print("DISCARD: {}".format(lfu))"""
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """
        . Must return the value in self.cache_data linked to key.
        . If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        """
        if key is None or key not in self.cache_data:
            return None
        # move the most recently used key to the end
        self.cache_count[key] += 1
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """ Removes the earliest item from the cache at MAX size
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut
