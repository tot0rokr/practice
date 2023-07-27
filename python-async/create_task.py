import asyncio

async def func(sec):
    print ("func")
    await asyncio.create_task(asyncio.sleep(sec))
    print ("func end")


def init():
    print ("init")
    task = asyncio.create_task(func(5))
    print ("init end")

    return task


async def main():
    print ("main")
    task = init()

    await task
    print ("main end")


if __name__ == '__main__':
    asyncio.run(main())
