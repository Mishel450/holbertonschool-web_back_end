#!/usr/bin/env python3
"""task-8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float and returns a multiply of that float"""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
