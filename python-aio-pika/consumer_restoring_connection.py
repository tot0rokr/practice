import asyncio
import logging

import aio_pika
from aio_pika.abc import AbstractIncomingMessage


async def on_message1(message: AbstractIncomingMessage) -> None:
    async with message.process():
        #  print(f" [x] Received {message!r}")
        print(f" [x] 1: getmessage")
        await asyncio.sleep(0.3)
        print(f" [x] 1: {message.body!r}")

async def on_message2(message: AbstractIncomingMessage) -> None:
    async with message.process():
        #  print(f" [x] Received {message!r}")
        print(f" [x] 2: getmessage")
        await asyncio.sleep(0.6)
        print(f" [x] 2: {message.body!r}")

async def on_message3(message: AbstractIncomingMessage) -> None:
    async with message.process():
        #  print(f" [x] Received {message!r}")
        print(f" [x] 3: getmessage")
        await asyncio.sleep(0.9)
        print(f" [x] 3: {message.body!r}")


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            connection = await aio_pika.connect_robust(
                    "amqp://guest:guest@localhost/",
            )
        except aio_pika.exceptions.AMQPConnectionError:
            print("Retry Connection")
            await asyncio.sleep(3)
        else:
            break

    queue_name = "test_queue"

    async with connection:
        # Creating channel
        channel = await connection.channel()

        # Will take no more than 10 messages in advance
        await channel.set_qos(prefetch_count=10)

        # Declaring queue
        queue1 = await channel.declare_queue(queue_name + "1")
        await queue1.consume(on_message1)
        # Declaring queue
        queue2 = await channel.declare_queue(queue_name + "2")
        await queue2.consume(on_message2)
        # Declaring queue
        queue3 = await channel.declare_queue(queue_name + "3")
        await queue3.consume(on_message3)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
