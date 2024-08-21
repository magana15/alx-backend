#!/usr/bin/env python3
""" caching module
"""
from base_caching import BaseCaching
from typing import Any, Optional


class BasicCache(BaseCaching):
    """  The Basic caching class
    """
    def put(self, key: Any, item: Any) -> None:
        """ Add data to the cache
            - Args:
                - key: new entry key
                - item: the value
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key: Any) -> Optional[Any]:
        """ Get the cache data associated with given key
            - Args:
                - the key to look for
            - Returns:
                - the value associated with the key
        """
        return self.cache_data.get(key)
