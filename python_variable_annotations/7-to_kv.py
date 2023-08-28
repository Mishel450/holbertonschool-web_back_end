#!/usr/bin/env python3
"""task-6"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string and a int/float and returns a tuple of them"""
    return (k, v)