#!/usr/bin/env python3
""" hypermedia pagination """
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    return (page * page_size - page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
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
        """ imp get_page """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dt = self.dataset()
        return dt[start_index: end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        next_page = (end_index + 1, page_size)
        prev_page = (end_index - 1, page_size)
        dts = self.dataset()
        total_pages = len(dts) / page_size
        return dict(page_size=page_size, page=page, data=data,
                    next_page=next_page, prev=prev_page, tt=total_pages)
