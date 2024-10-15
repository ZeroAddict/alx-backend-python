#!/usr/bin/env python3
"""
BasicSyntax of async
Writes a asynchronous coroutine
Takes integer argument max_delay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine: wait_random waits for a random delay between 0 and max_delay (included and float value)
    seconds and then returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
