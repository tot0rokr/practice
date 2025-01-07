import asyncio


async def asyn():
    print("async")


def sync():
    print("sync")
    loop = asyncio.get_running_loop()
    loop.run_until_complete(asyn())


async def main():
    print("main")
    sync()


if __name__ == '__main__':
    asyncio.run(main())
