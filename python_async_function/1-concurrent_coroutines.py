#!/usr/bin/env python3
"""task-1"""
import asyncio
from random import uniform
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task-0"""
    the_list = []
    for i in range(n):
        w_r = await wait_random(max_delay)
        the_list.append(w_r)
    the_list = sorted(the_list)
    return (the_list)
