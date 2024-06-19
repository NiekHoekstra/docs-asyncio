"""
Demonstrates use of the 'Future' object.

The 'future' object allows for light communication between tasks.
It allows one task to block until another task can give the signal to continue.
"""

import asyncio


async def slow_task(future: asyncio.Future):
    print('One', flush=True)
    await asyncio.sleep(1.0)
    future.set_result(True)
    print('Two', flush=True)
    await asyncio.sleep(1.0)
    print('Three', flush=True)
    return 100


async def main():
    future = asyncio.Future()
    task = asyncio.create_task(slow_task(future))
    print('Waiting for the future.', flush=True)
    await future
    print('Back from the future!', flush=True)
    await task


asyncio.run(main())
