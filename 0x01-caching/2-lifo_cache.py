#!/usr/bin/env python3
"""
The LIFO caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class LIFOCache(BaseCaching):
    """ The LIFO cache class
    """

    def put(self, key: Any, item: Any) -> None:
        """ Add the data to the cache based on LIFO algo
            - Args:
                - key: new entry key
                - item: key's value
        """
        if not key or not item:
            return
        new_cache_data = {key: item}
        if len(self.cache_data) == self.MAX_ITEMS:
            cache_keys = list(self.cache_data.keys())
            key_to_remove = cache_keys[-1]
            self.cache_data.pop(key_to_remove)
            print(f'DISCARD: {key_to_remove}')
        self.cache_data.update(new_cache_data)

    def get(self, key: Any) -> Optional[Any]:
        """ Get the cache data associated with the given key
            - Args:
                - The key to look for
            - Returns:
                - The value associated with the key
        """
        return self.cache_data.get(key)
