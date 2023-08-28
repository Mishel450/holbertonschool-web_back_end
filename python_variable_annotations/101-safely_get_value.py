#!/usr/bin/env python3
"""task-100"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, T] = None):
    if key in dct:
        return dct[key]
    else:
        return default
