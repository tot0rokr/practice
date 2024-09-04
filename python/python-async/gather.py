import asyncio
import time

async def test(n):
    for _ in range(n):
        print(round(time.time()), n)
        await asyncio.sleep(1)

async def cpu_bound(n):
    def fibo(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibo(n-1) + fibo(n-2)

    print(round(time.time()), n, fibo(n))

async def main():
    loop = asyncio.get_running_loop()

    await asyncio.gather(test(1), test(2), test(3), test(4), test(5), cpu_bound(36))


asyncio.run(main())
