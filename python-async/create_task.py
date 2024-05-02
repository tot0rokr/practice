import asyncio


def callback(fut):
    try:
        exc = fut.exception()
        print(type(exc), exc)
    except asyncio.CancelledError:
        print("Cancelled")

async def func(sec):
    print ("func")
    await asyncio.create_task(asyncio.sleep(sec))
    1/0
    print ("func end")


def init():
    print ("init")
    task = asyncio.create_task(func(5))
    task.add_done_callback(callback)
    print ("init end")

    return task


async def main():
    print ("main")
    task = init()

    await task
    print ("main end")


if __name__ == '__main__':
    asyncio.run(main())
