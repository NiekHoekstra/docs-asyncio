import asyncio


async def lazy_range(start, end):
    for i in range(start, end):
        await asyncio.sleep(1)
        yield i


# __aiter__
# __anext__

async def main():
    async for i in lazy_range(0, 10):
        print(i)


asyncio.run(main(), debug=True)
