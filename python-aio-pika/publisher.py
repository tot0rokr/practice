import asyncio

import aio_pika

import random


async def main() -> None:
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@localhost/",
    )

    async with connection:

        channel = await connection.channel()

        for i in range(30):
            routing_key = "test_queue" + str(random.randint(1, 3))
            await channel.default_exchange.publish(
                aio_pika.Message(body=f"Hello {routing_key}".encode(), delivery_mode=aio_pika.DeliveryMode.PERSISTENT,),
                routing_key=routing_key,
            )


if __name__ == "__main__":
    asyncio.run(main())
