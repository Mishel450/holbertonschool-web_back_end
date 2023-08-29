#!/usr/bin/env python3
"""task-2"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """task-2"""
    time1 = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    time2 = time.time()
    total_time = time2 - time1
    return (total_time)
