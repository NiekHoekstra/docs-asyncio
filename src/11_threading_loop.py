import threading
import asyncio


async def run_in_thread(func, args, kwargs):
    handle = threading.Event()
    thread = asyncio.to_thread(func, handle, *args, **kwargs)
    try:
        return await thread
    except asyncio.CancelledError:
        handle.set()


def my_loop(handle: threading.Event):
    while not handle.is_set():
        ...
