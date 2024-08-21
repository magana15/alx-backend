#!/usr/bin/env python3
"""
 The LFU caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class LFUCache(BaseCaching):
    """ The LFU cache class
    """
    def __init__(self):
        """ Initialize a new instance
        """
        super().__init__()
        self.counter = {}

    def put(self, key: Any, item: Any) -> None:
        """ Add the data to the cache based on LRU algo
            - Args:
                - key: new entry key
                - item: key's value
        """
        if not key or not item:
            return
        counter = self.counter
        new_cache_data = {key: item}
        old_cache_data = self.cache_data.get(key)
        if len(self.cache_data) == self.MAX_ITEMS and not old_cache_data:
            key_to_remove = list(counter.keys())[0]
            self.cache_data.pop(key_to_remove)
            counter.pop(key_to_remove)
            print(f'DISCARD: {key_to_remove}')
        self.cache_data.update(new_cache_data)
        counter.update({key: counter.get(key, 0) + 1})
        counter = dict(sorted(counter.items(),
                              key=lambda x: (x[1], x[0])))

    def get(self, key: Any) -> Optional[Any]:
        """ Get the cache data associated with given key
            and update dict accordingly
            - Args:
                - the key to look for
            - Return:
                - the value associated with the key
        """
        cache_item = self.cache_data.get(key)
        counter = self.counter
        if cache_item:
            counter.update({key: counter.get(key) + 1})
            counter = dict(sorted(counter.items(),
                                  key=lambda x: (x[1], x[0])))
        return cache_item
