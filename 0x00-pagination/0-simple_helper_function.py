#!/usr/bin/env python3
""" Page index module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Gets the start and end indices of a dataset
        - Args:
            - page: page to look for information
            - page_size: size of each page
        - Return:
            - tuple of start_index and end_index of each page
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
