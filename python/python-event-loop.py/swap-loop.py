import asyncio


loop = asyncio.get_event_loop()

async def proc(n):
    for i in range(n):
        print(i)
        await asyncio.sleep(1)


def swapper():
    print("swapper")
    if loop.is_running():
        print("running")
        tmp_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(tmp_loop)
        loop.stop()
        tmp_loop.run_until_complete(proc())
        asyncio.set_event_loop(loop)
    else:
        loop.run_until_complete(proc(3))

async def a_swapper():
    swapper()

loop.create_task(proc(100))


swapper()
asyncio.run(a_swapper())
