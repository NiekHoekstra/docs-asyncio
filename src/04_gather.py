"""
Demonstration of `gather(...)` and its usefulness.
"""
import asyncio
import random
import time
from asyncio import Future
from typing import Coroutine


async def delayed(label) -> float:
    """
    Waits for a random number of seconds, then return the time waited.
    :param label: Label to use when printing to the console.
    :return: Total delay within the function.
    """
    print(f'start {label}')
    # don't sleep longer than 5 seconds, that's silly.
    delay = random.random() * 5
    await asyncio.sleep(delay)
    # time.sleep(delay)
    print(f'end {label}')
    return delay


async def main():
    # This creates 5 tasks, each with an index.
    coroutines: list[Coroutine] = [delayed(i) for i in range(5)]
    print('Did we start yet?')
    start = time.time()
    # asyncio.gather(*coroutines) creates a 'future' that will execute *all* of the coroutines it has been given.
    # This is roughly equivalent to creating a background task.
    # The values are return in the same order as the tasks it was given.
    concurrent: Future = asyncio.gather(*coroutines)
    # In this case,
    delay_per_task = await concurrent
    end = time.time()
    print(f'Done in {end - start:.2f} seconds!')
    print(f'Total time delay: {sum(delay_per_task):.2f} seconds.')


asyncio.run(main())
# ---
# Exercise 1: replace `await asyncio.sleep(delay)` with `time.sleep(delay)`.
# Don't forget to remove the 'await' keyword there.
# ---
# Exercise 2:  Immediately after asyncio.gather, print all tasks as shown in `03_task.py`.
# ---
# Exercise 3: Treat 'concurrent' like a task, and try polling it with `task.done()` as shown in `03_task.py`.
# ---
