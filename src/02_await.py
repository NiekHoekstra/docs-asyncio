"""
Demonstration of coroutines, 'await', and `asyncio.sleep`.

This only demo's linear code, and provides no actual benefit of async code just jet.
It is only meant to illustrate how a parallel for synchronous code.
"""
import asyncio
import logging
import time

# Any logging from asyncio is shown in the standard error output.
logging.getLogger('asyncio').addHandler(logging.StreamHandler())


async def read_5():
    """Pretend data is being read by waiting 5 seconds."""
    print('long start')
    await asyncio.sleep(5)
    print('long end')


async def read_1():
    """Pretend data is being read by waiting 1 second."""
    print('short start')
    await asyncio.sleep(1)
    print('short end')


async def main():
    # Although 'await' is used, this code still runs synchronously.
    start = time.time()
    await read_1()
    await read_5()
    await read_1()
    end = time.time()
    print(f'Done in {end - start:.2f} seconds.')


asyncio.run(main())
# --
# Exercise 1: remove the 'await' keyword and see what happens to the execution time and watch the console output.
# --
