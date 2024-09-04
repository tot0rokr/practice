import asyncio

async def main():
    print ("main")
    task = None

    await asyncio.Task()
    print ("main end")


if __name__ == '__main__':
    asyncio.run(main())
