#!/usr/bin/env python3
"""task-6"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of ints and floats and returns a sum of them"""
    sum = 0.00
    for i in mxd_lst:
        sum += i
    return sum
