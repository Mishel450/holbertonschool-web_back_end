#!/usr/bin/env python3
"""task-1"""
import asyncio
from random import uniform
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task-0"""
    delays: List[float] = []
    tasks: List = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)
    return delays
