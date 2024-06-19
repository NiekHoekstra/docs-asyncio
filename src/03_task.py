"""
Demonstration of 'create_task'.

This is where the features of asyncio really get to shine.
"""
import asyncio
import time

assert time


async def read_big():
    await asyncio.sleep(0.5)
    print('big')
    return 1000


async def main():
    # Like before, first create a coroutine.
    coro = read_big()
    # Instead of using 'await', use asyncio.create_task.
    # This puts the task on its own flow.
    task = asyncio.create_task(coro, name='Big')

    # This current 'loop' can be inspected, printing all the associated tasks.
    for entry in asyncio.all_tasks():
        print('Task:', entry)

    # The 'task' system puts a few extras
    while not task.done():
        print('.', end='', flush=True)
        await asyncio.sleep(0.1)
        # time.sleep(0.1)
    print(task.result())


asyncio.run(main())
# ---
# Exercise 1: replace `await asyncio.sleep(0.1)` with `time.sleep(0.1)`.
# ---
# Exercise 2: Print the list of tasks after `print(task.result())`
# ---
# Exercise 3: Remove the entire 'while' loop, and replace it with `await task`.
# ---
# Exercise 4: Raise an exception in `read_big`.
# ---
# Exercise 5: Remove `print(task.result())` and play around with `task.cancel()` at various lines  in the code.
# When comfortable with it, restore `print(task.result())` and see if you understand what happened.
# ---
