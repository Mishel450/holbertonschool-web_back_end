#!/usr/bin/env python3
"""task-0"""
import asyncio
from random import uniform


async def wait_random(max_delay=10):
    """task-0"""
    rand_float = uniform(0, max_delay)
    await asyncio.sleep(rand_float)
    print(rand_float)
