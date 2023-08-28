#!/usr/bin/env python3
"""task-1"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    a_list = asyncio.run(wait_n(n, max_delay))
    total_time = 0.00
    for i in a_list:
        total_time += i
    the_time = total_time / n
    return the_time
