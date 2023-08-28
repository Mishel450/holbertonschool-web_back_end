#!/usr/bin/env python3
"""task-9"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """task-9"""
    return [(i, len(i)) for i in lst]
