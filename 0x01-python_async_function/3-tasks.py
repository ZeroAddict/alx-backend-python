#!/usr/bin/env python3
"""
Module runs to return aycio.Task
Write function task_wait_random, takes max_delay as int
Returns a asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random function
    takes integer arg max_delay
    Returns a async.Task
    """
    stop = asyncio.create_task(wait_random(max_delay))
    return stop
