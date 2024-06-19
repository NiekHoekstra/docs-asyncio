import asyncio
import gc

my_queue = asyncio.Queue()


async def queue_worker():
    while True:
        result, number = await my_queue.get()  # type: asyncio.Future, int
        result.set_result(number * 2)
        my_queue.task_done()


async def main():
    t = asyncio.create_task(queue_worker())
    for i in range(800):
        future = asyncio.Future()
        my_queue.put_nowait((future, i))
        await future
        print(future.result())
        await asyncio.sleep(future.result() * 0.01)
        gc.collect()

    try:
        await asyncio.wait_for(asyncio.shield(t), 4.0)
    except TimeoutError:
        pass


asyncio.run(main(), debug=True)
