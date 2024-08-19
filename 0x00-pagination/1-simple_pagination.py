#!/usr/bin/env python3
""" the pagination module
"""
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular babynames.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Retrieves dataset for specific page
            - Args:
                - page: search page
                - page_size: size of each page
            - Return:
                - list of a dataset for the specified page
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start: end]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Gets start and end indices of dataset
        - Args:
            - page: a page to look for the information
            - page_size: the size of each page
        - Return:
            - a tuple of startindex and endindex of each page
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
