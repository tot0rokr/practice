import asyncio
from functools import partial
import signal
import time
import os

def wrap_signal(signum: int, frame):
    signal.raise_signal(signal.SIGUSR1)

signal.signal(signal.SIGINT, wrap_signal)
signal.signal(signal.SIGTERM, wrap_signal)


shutdown: bool = False

def sig_handler(loop, futures, awaits) -> None:
    """ signal handler. `print_and_sleep`의 무한루프를 종료시킨다. """
    print('stopping loop...')
    #  global shutdown
    #  shutdown = True
    for fut in futures:
        fut.cancel()
    #  loop.create_task(asyncio.sleep(1))
    loop.stop()
    loop.create_task(hello(1))
    loop.run_until_complete(hello(1))


async def hello(n=3):
    print("hello start")
    await asyncio.sleep(n)
    print("hello end")


async def print_and_sleep(loop) -> None:
    """ 1초에 한번 `sleep`이라는 문자를 출력하는 무한루프 """
    while True:
        print('sleep')
        await asyncio.sleep(1)


async def send_sigterm_after_3_seconds() -> None:
    """ 3초 이후에 스크립트 자신에게 SIGTERM을 보낸다. """
    await asyncio.sleep(3)
    os.kill(os.getpid(), signal.SIGTERM)


def main() -> None:
    loop = asyncio.get_event_loop()
    futures = []
    awaits = []

    loop.add_signal_handler(signal.SIGUSR1, partial(sig_handler, loop, futures, awaits))

    futures.append(loop.create_task(print_and_sleep(loop)))
    futures.append(loop.create_task(send_sigterm_after_3_seconds()))
    awaits.append(hello())

    loop.run_forever()
    print('loop stopped')
    time.sleep(1)
    #  print(loop.run_until_complete(asyncio.gather(*futures, return_exceptions=True)))
    #  print(loop.run_until_complete(asyncio.gather(*awaits, return_exceptions=True)))
    loop.close()
    print('loop closed')


if __name__ == '__main__':
    main()
