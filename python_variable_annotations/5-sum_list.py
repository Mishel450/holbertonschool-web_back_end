#!/usr/bin/env python3
"""task-3"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats and sum them"""
    a = 0.00
    for i in input_list:
        a += i
    return a
