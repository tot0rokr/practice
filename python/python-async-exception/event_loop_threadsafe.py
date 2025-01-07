import asyncio
from threading import Thread

def main():
    loop = asyncio.get_event_loop()

    thread = Thread(target=loop.run_forever)
    thread.start()

    async def test(n):
        await asyncio.sleep(n)
        print(f"test({n})")
        raise Exception(f"test({n}) !!!!!!!!!!!!!!!!!!!!!!!!!!")

    fut = asyncio.run_coroutine_threadsafe(test(3), loop)
    try:
        print("result", fut.result())
    except Exception:
        print("exception", fut.exception())
    loop.call_soon_threadsafe(loop.stop)

    thread.join()

if __name__ == '__main__':
    main()
