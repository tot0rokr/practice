import tracemalloc
import asyncio
from contextlib import contextmanager, suppress
import gc
import time

gc.set_threshold(700,10,10)

TEST_COUNT = 1000000

class Work:
    """Work structure."""
    __next_index = 1000

    def __init__(self, func, *args, **kwargs):
        self.index = self.__new_index()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    async def run(self):
        await self.func(*self.args, **self.kwargs)

    @classmethod
    def __new_index(cls) -> int:
        index = cls.__next_index
        cls.__next_index += 1
        return index

class WorkScheduler:
    def __init__(self):
        self.__works: dict[int, asyncio.Task] = {}

    def register(self, loop: asyncio.AbstractEventLoop, work: Work) -> None:
        task = loop.create_task(work.run())
        task.add_done_callback(lambda _: self.unregister(work.index))
        self.__works[work.index] = task

    def unregister(self, index: int) -> None:
        with suppress(KeyError):
            task = self.__works.pop(index)
            task.cancel()

    def stop(self) -> None:
        for task in self.__works.values():
            task.cancel()

        self.__works.clear()

async def func():
    await asyncio.sleep(1000)

async def test1(wq):
    for i in range(TEST_COUNT):
        work = Work(func)
        wq.register(asyncio.get_running_loop(), work)
        await asyncio.sleep(0)
        wq.unregister(work.index)

async def test2(wq):
    for i in range(TEST_COUNT):
        work = Work(func)
        wq.register(asyncio.get_running_loop(), work)
    await asyncio.sleep(0)
    wq.stop()

async def test3(wq):
    for i in range(TEST_COUNT):
        work = Work(func)
        wq.register(asyncio.get_running_loop(), work)
    await asyncio.sleep(0)

async def test4(wq):
    pass

@contextmanager
def monitoring():
    tracemalloc.start()

    before = time.time()
    yield
    after = time.time()
    print("running time:", after - before)

    print("using memory(curr, peak):", tracemalloc.get_traced_memory())
    tracemalloc.stop()

    obj = gc.get_count()
    gc.collect()
    print("gc object (before, after collect):", obj, gc.get_count())
    print()


for f in [test1, test2, test3, test4]:
    wq = WorkScheduler()
    with monitoring():
        asyncio.run(f(wq))
    wq.stop()
    del wq
