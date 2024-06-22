"""
Queues are a way for asyncio to communicate a bit of data.
It can be desirable to have a background task whose sole function is communication.

This means one async task could be listening to a message queue,
and makes a different task process it.
Otherwise, messages in that queue can become a backlog.
"""
import asyncio

# A Queue is created,
# One task will put items in, another task will pull objects out.
my_queue = asyncio.Queue(8)


async def queue_worker():
    """
    Loops, working through the global queue, multiplies each object by 2.
    """
    while True:
        callback, number = await my_queue.get()  # type: asyncio.Future, int
        callback.set_result(number * 2)
        await asyncio.sleep(1.0)
        my_queue.task_done()


async def main():
    # Assigning the loop for create_future().
    loop = asyncio.get_event_loop()
    # Create the worker, and make it a task.
    worker: asyncio.Task = loop.create_task(queue_worker())
    futures: list[asyncio.Future] = []
    for i in range(800):
        future = loop.create_future()
        future.add_done_callback(lambda f: print(f.result()))
        # The queue has an infinite size, no need to wait for the queue to have space.
        await my_queue.put((future, i))
        await asyncio.sleep(0.0)
        print('.', end='', flush=True)
    try:
        print('waiting for exit.')
        await asyncio.wait_for(worker, 4.0)
        print('Task ended')
    except TimeoutError:
        print('Killed task.')


asyncio.run(main(), debug=True)
# ---
# Exercise 1: Use the `future.add_done_callback(...)` to print the result.
# Note that this method does not accept an async function as a callback.
# --
# Exercise 2
# 1. Put a delay in the worker
# 2. Put a maximum size on my_queue.
# 3. Change `my_queue.put_nowait(...)` to `await my_queue.put(...)`
# 4. Add in a couple of print statements to see when the program seems to slow down.
# ---
