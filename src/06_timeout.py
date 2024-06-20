"""
The 'timeout' system can stop a coroutine after a certain duration.
"""
import asyncio
import time


async def main():
    # These are three calls which 'timeout' at verious points.
    print(f'{using_context_decorator.__name__} {await using_context_decorator():.2f}s')
    print(f'{using_function.__name__} {await using_function():.2f}s')
    print(f'{using_shield.__name__} {await using_shield():.2f}s')


async def using_context_decorator():
    """
    Demonstrate usage of a timeout using a context decorator.
    Context decorators can be a bit bulky because they add indent.
    :return: Time passed.
    """
    start = time.time()
    try:
        # upon entering a timeout, it starts running.
        # After a certain amount of time, it must have left the indented block or it will raise a TimeoutError.
        async with asyncio.timeout(1) as timer:
            await asyncio.sleep(10)
    except TimeoutError:
        pass
    return time.time() - start


async def using_function():
    """
    It's possible to wrap a coroutine in a timeout object.
    This also allows developers to return coroutines with a timeout already associated with them.
    :return: Time passed since the start.
    """
    start = time.time()
    delay = asyncio.sleep(10)
    # The indentation isn't always very pretty.
    # In these situations, the wait_for(...) can feel more readable.
    try:
        await asyncio.wait_for(delay, 1.0)
    except TimeoutError:
        pass
    return time.time() - start


async def using_shield():
    """
    Waiting usually aborts the coroutine being run, but what if that is not desirable?
    :return: Time passed since start.
    """
    # Our friendly 'delay' will pretend to do a lot of work for us.
    delay = asyncio.sleep(5.0)
    # For a shield to work, it usually has to be put in a task.
    # Remember that the task is immediately added to the list of tasks, so any 'await' will make it run.
    task = asyncio.create_task(delay)

    # Create a 'shielded' version of the task.
    # This can be used like a regular task in most cases.
    # When the `.cancel()` method is called on the shield, it simply stops waiting.
    safe_task = asyncio.shield(task)
    start = time.time()
    try:
        # After 1 second, the
        await asyncio.wait_for(safe_task, 1.0)
    except TimeoutError:
        pass
    print(f'{time.time() - start} seconds passed, still waiting.')
    # Continue waiting (in a blocking manner this time).
    await task
    return time.time() - start

asyncio.run(main(), debug=True)
