#!/usr/bin/env python3

import asyncio
from typing import List
import random

"""
Execute multiple coroutines same time with async
Write async coroutine
takes argument wait_n and max_delay.

Args:
    max_delay (int): Maximum delay in seconds.

Returns:
    float: Time elapsed.
"""

# Importing from another module

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine with type anniotation executes
    multiple wait_random tasks concurrently
    wait_n defined as an async spins wait_random

    Args:
        n (int): Number of tasks to execute.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of time elapsed for each task.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    stop_task = [await task for task in asyncio.as_completed(tasks)]
    return stop_task
