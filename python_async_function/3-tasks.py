#!/usr/bin/env python3
"""task-0"""
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> Task:
    """task-3"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
