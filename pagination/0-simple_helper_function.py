#!/usr/bin/env python3
"""task-0"""


def index_range(page, page_size):
    """return a tuple of the start and the end of the page"""
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return (start_page, end_page)
