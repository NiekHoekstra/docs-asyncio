import asyncio
import time


def thread_me(message):
    print(message, flush=True)


async def no_wait():
    time.sleep(3.0)


async def main():
    coroutine = asyncio.to_thread(thread_me, 'hello world')

    await asyncio.sleep(3.0)
    print('...')
    task = asyncio.create_task(coroutine)
    await no_wait()  # asyncio.sleep(3.0)
    print('...')
    # await task
    # while not task.done():
    #     print('.', end='', flush=True)
    #     await asyncio.sleep(0.1)
    #     # time.sleep(0.1)
    # print(task.result())


asyncio.run(main())
