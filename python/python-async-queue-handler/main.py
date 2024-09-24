import asyncio

class CustomQueue(asyncio.Queue):
    def __init__(self, maxsize=0, on_full=None, *args, **kwargs):
        super().__init__(maxsize, *args, **kwargs)
        self.on_full = on_full  # 큐가 꽉 찼을 때 호출할 핸들러

    async def put(self, item):
        if self.full():
            if self.on_full:
                self.on_full(self)  # 큐가 꽉 찼을 때 핸들러 호출
        await super().put(item)  # 원래의 put 함수 실행

# 큐가 꽉 찼을 때 호출되는 핸들러
def queue_full_handler(queue):
    print(f"Queue is full! Current size: {queue.qsize()}")

async def producer(queue):
    for i in range(10):
        print(f"Producing item {i}")
        await queue.put(i)
        await asyncio.sleep(0.5)

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consuming item {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def main():
    # 큐의 크기를 3으로 설정하고, 꽉 찼을 때 호출되는 핸들러 등록
    queue = CustomQueue(maxsize=3, on_full=queue_full_handler)

    # Producer와 Consumer 실행
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await queue.join()  # 모든 아이템이 처리될 때까지 대기
    consumer_task.cancel()

# 실행
asyncio.run(main())

