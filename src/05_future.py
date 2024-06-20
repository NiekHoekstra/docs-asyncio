"""
Demonstrates use of the 'Future' object.

The 'future' object allows for light communication between tasks.
It allows one coroutine to block until another coroutine gives the signal to continue.
"""

import asyncio


async def big_database_thing(future: asyncio.Future):
    """
    Pretends this is a big database thing/
    :param future: Callback
    """
    name = asyncio.current_task().get_name()
    print(f'{name}: Doing database things', flush=True)
    await asyncio.sleep(1.0)
    print(f'{name}: Saving results')
    await asyncio.sleep(1.0)
    print(f'{name}: Returning Results')
    # 'Future' is being given a result.
    # Any objects waiting for this will get 'unstack' when the next 'await' is reached.
    future.set_result([1, 2, 3, 4])
    # The 'request' is finished.
    # Now clean up the mess you made, flush pending change, maybe send some data to an analytics endpoint.
    print(f'{name}: Cleanup start', flush=True)
    await asyncio.sleep(1.0)
    # This means the caller doesn't have to wait for cleanup to occur and can just finish its own processing
    # while this happens in the background.
    print(f'{name}: Cleanup end', flush=True)


async def main():
    # Create a basic Future
    future = asyncio.Future()
    # Put the 'future' in another coroutine.
    coro = big_database_thing(future)
    # Let the coroutine run in the background.
    task = asyncio.create_task(coro)
    # Wait for the future object to call back.
    print('Waiting for the future.', flush=True)
    result = await future
    print('Got results!', result)
    await task


asyncio.run(main())
# ---
# Exercise 1: Instead of `set_result`, use `set_exception` to see how that works.
# ---
# Exercise 2: Remove the task entirely. Put a result in the future, and immediately await it.
# ---
# Exercise 3: Is it safe to await the same Future object multiple times?
# ---
