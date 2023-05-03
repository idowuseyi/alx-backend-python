#!/usr/bin/env python3
"""Contains a coroutine that delays a certain amount of time and returns it"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns a random float between 0 and max_delay
    Args:
        max_delay: The maximum delay value to return
    Returns:
        A random float value between 0 and max_delay value
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
