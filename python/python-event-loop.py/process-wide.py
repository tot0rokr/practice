# loop와 loop2 는 동일한 자료구조로 취급받지만, 프로세스간 영향을 주지는 않는다.
import asyncio
import time
import multiprocessing

loop = asyncio.get_event_loop()

def check():
    loop2 = asyncio.get_event_loop()
    loop2.run_until_complete(asyncio.sleep(5))
    print(loop == loop2, loop is loop2)

def new_loop():
    loop2 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop2)
    print(loop == loop2, loop is loop2)

mp = multiprocessing.get_context("fork")
p = mp.Process(target=check)
p.start()
loop.run_until_complete(asyncio.sleep(2))
loop.stop()
loop.close()
print("main loop close")
p.join()

p = mp.Process(target=new_loop)
p.start()
p.join()
