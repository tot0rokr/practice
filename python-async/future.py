import asyncio

async def test(n, future):
    for _ in range(n):
        print(n)
        await asyncio.sleep(1)

    future.set_result(0)

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    task1 =  asyncio.create_task(test(5, future))
    await task1
    task2 =  asyncio.create_task(test(5, future))
    await task2
    task3 =  asyncio.create_task(test(5, future))
    await task3
    await future


asyncio.run(main())
