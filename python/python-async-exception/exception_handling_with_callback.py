import asyncio
from threading import Thread

def exception_handler(loop, context):
    print("exception handling: ", context["exception"])
    loop.stop()

def main():
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(exception_handler)

    async def test(n):
        await asyncio.sleep(n)
        print(f"test({n})")
        raise Exception(f"test({n}) !!!!!!!!!!!!!!!!!!!!!!!!!!")

    def callback(fut):
        if fut.exception() is not None:
            print("callback: " + str(fut.exception()))
            raise fut.exception()

    loop.create_task(test(3)).add_done_callback(callback)

    loop.run_forever()

if __name__ == '__main__':
    main()

