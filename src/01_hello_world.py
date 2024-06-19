"""
Simple 'Hello World' using asyncio.

This module presents a basic 'Hello World'.
Nothing interesting happens here.
"""
import asyncio
from typing import Coroutine


# Async functions are marked with the 'async' keyword.
# This tells Python that it has to provide certain functionality for it.
async def hello_world() -> int:
    print('Hello')
    return 1


# When calling an async function, it returns a coroutine.
# Just like a generator, no actual code execute has been taken place yet.
# If any arguments were provided, they are now tied to the
coro: Coroutine[None, None, int] = hello_world()

# The type hint for Coroutine can be read like this:
# Coroutine[YieldType, SendType, ReturnType]
# There are better ways of writing this, those will be shown later.

print(f'{coro=}')

# In order to actually execute a coroutine, it needs an async environment.
# The asyncio module provides this. In this case `asyncio.run` will do just that.
result = asyncio.run(coro, debug=True)
print(f'{result=}')

# Nothing interesting has happened here.
# The async keyword has been shown, but nothing async specific has happened yet.
