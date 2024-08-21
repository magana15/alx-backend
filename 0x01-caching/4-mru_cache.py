#!/usr/bin/env python3
"""
The MRU caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class MRUCache(BaseCaching):
    """ The MRU cache class
    """
    def put(self, key: Any, item: Any) -> None:
        """ Add the data to the cache based on LRU algo
            - Args:
                - key: new entry key
                - item: key's value
        """
        if not key or not item:
            return
        new_cache_data = {key: item}
        if len(self.cache_data) == self.MAX_ITEMS:
            key_to_remove = list(self.cache_data.keys())[-1]
            self.cache_data.pop(key_to_remove)
            print(f'DISCARD: {key_to_remove}')
        self.cache_data.update(new_cache_data)

    def get(self, key: Any) -> Optional[Any]:
        """ Get the cache data associated with given key
            and update dict in accordingly
            - Args:
                - the key to look for
            - Return:
                - the value associated with the key
        """
        cache_item = self.cache_data.get(key)
        if cache_item:
            self.cache_data.pop(key)
            self.cache_data.update({key: cache_item})
        return cache_item
