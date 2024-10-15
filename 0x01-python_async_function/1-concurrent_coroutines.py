#!/usr/bin/env python3

import asyncio
from typing import List
import random

"""
Execute multiple coroutines same time with async
Write async coroutine
takes argument wait_n and max_delay
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine
    wait_n defined as an async spins wait_random
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    stop_task = [await task for task in asyncio.as_completed(tasks)]
    return stop_task
