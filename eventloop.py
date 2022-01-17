import asyncio

loop = asyncio.get_event_loop()
loop02 = asyncio.get_event_loop()

print(loop == loop02)