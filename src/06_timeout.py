import asyncio


async def long_task():
    await asyncio.sleep(8)
    print('That was a nice nap.')


async def main_ugly():
    my_task = long_task()
    try:
        async with asyncio.timeout(5) as timer:
            await my_task
    except TimeoutError:
        pass
    print(timer.expired())
    print(my_task)


async def main_pretty():
    my_task = long_task()
    try:
        print(my_task, my_task.cr_running)
        await asyncio.wait_for(my_task, 1.0)
    except TimeoutError:
        pass
    await my_task


async def main_resistant():
    my_task = long_task()
    safe_task = asyncio.shield(my_task)
    try:
        await asyncio.wait_for(safe_task, 1.0)
    except TimeoutError:
        pass
    await safe_task


asyncio.run(main_resistant(), debug=True)
