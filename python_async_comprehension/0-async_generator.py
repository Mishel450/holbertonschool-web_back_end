#!/usr/bin/env python3
"""task-0"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator generates a 10 random floats"""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
