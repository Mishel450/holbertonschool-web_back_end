#!/usr/bin/env python3
"""task-2"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """return a tuple of the start and the end of the page"""
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return (start_page, end_page)


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
        """gets the values of the csv file"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        the_pages = index_range(page, page_size)
        self.dataset()
        return self.__dataset[the_pages[0]:the_pages[1]]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """gets the values and returns a dict"""
        self.dataset()
        if self.__dataset[page - 1]:
            prev_page = None
        else:
            prev_page = page - 1
        if self.__dataset[page + 1]:
            next_page = None
        else:
            next_page = page + 1
        the_dict = {'page_size': page_size,
                    'page': page,
                    'data': self.__dataset[page:page + page_size],
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': len(self.__dataset[:])}
        return the_dict

