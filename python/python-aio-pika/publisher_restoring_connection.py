import asyncio

import aio_pika

import random


async def main() -> None:
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

    await asyncio.sleep(10)
    async with connection:

        channel = await connection.channel()

        for i in range(30):
            routing_key = "test_queue" + str(random.randint(1, 3))
            while True:
                try:
                    await channel.default_exchange.publish(
                        aio_pika.Message(body=f"Hello {routing_key}".encode(), delivery_mode=aio_pika.DeliveryMode.PERSISTENT,),
                        routing_key=routing_key,
                    )
                except aio_pika.exceptions.ChannelInvalidStateError:
                    print("Retry Publish")
                    await asyncio.sleep(3)
                else:
                    break

            print(f"publish {routing_key}")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
