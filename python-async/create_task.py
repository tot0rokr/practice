import asyncio


def callback(fut, task):
    try:
        exc = fut.exception()
        print(type(exc), exc)
    except asyncio.CancelledError:
        print("Cancelled")

    if fut is task:
        print("fut is task")

async def func(sec):
    print ("func")
    await asyncio.create_task(asyncio.sleep(sec))
    1/0
    print ("func end")


def init():
    print ("init")
    task = asyncio.create_task(func(3))
    task.add_done_callback(lambda fut: callback(fut, task))
    print ("init end")

    return task


async def main():
    print ("main")
    task = init()

    await task
    print ("main end")


if __name__ == '__main__':
    asyncio.run(main())
