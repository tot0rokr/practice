import asyncio

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

    runners = []
    runners.append(loop.create_task(test(3)))
    k = loop.create_task(test(4))
    loop.create_task(test(5))


    loop.run_forever()

if __name__ == '__main__':
    main()
