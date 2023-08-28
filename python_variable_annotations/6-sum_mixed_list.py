#!/usr/bin/env python3
"""task-6"""
from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    """takes a list of ints and floats and returns a sum of them"""
    sum = 0.00
    for i in mxd_lst:
        sum += i
    return sum
