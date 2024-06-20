import asyncio


class MyContext:
    async def __aenter__(self):
        await asyncio.sleep(1.0)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(1.0)


async def main():
    async with MyContext():
        pass


asyncio.run(main(), debug=True)
