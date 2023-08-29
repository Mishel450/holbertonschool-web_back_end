#!/usr/bin/env python3
"""task-2"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """task-2"""
    time1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    time2 = time.time()
    total_time = time2 - time1
    return (total_time / n)