import asyncio
import threading
import time


def hello_thread():
    time.sleep(1.4)
    print('Thread:', threading.current_thread().ident, flush=True)


def thread_me(message):
    print(message, flush=True)


async def no_wait():
    time.sleep(3.0)


async def main():
    hello_thread()
    coroutine = asyncio.to_thread(hello_thread, )
    print('Proving it does not auto-launch.', flush=True)
    await asyncio.sleep(3.0)
    print('launching')
    # Remember that tasks do not start executing until an 'await' has occurred.
    task = asyncio.create_task(coroutine)
    # This sleep simply lets asyncio cycle through its tasks until it's this function's turn again.
    await asyncio.sleep(0.0)
    print('Should not be finished yet.', flush=True)
    # Synchronous sleep, to prove a point.
    time.sleep(2.0)
    print('Should be finished.', flush=True)
    await no_wait()  # asyncio.sleep(3.0)
    print('...')
    hello_thread()
    # await task
    # while not task.done():
    #     print('.', end='', flush=True)
    #     await asyncio.sleep(0.1)
    #     # time.sleep(0.1)
    # print(task.result())


asyncio.run(main())
