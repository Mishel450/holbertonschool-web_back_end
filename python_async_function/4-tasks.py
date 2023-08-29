#!/usr/bin/env python3
"""task-1"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """task-0"""
    list_random = []
    for _ in range(n):
        list_random.append(await task_wait_random(max_delay))
    return sorted(list_random)
