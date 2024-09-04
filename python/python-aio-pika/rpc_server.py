import asyncio
import logging

from aio_pika import Message, connect
from aio_pika.abc import AbstractIncomingMessage


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def get_on_call(exchange) -> None:
    async def on_call(message):
        await on_call_wrapper(exchange, message)
    return on_call


async def on_call_wrapper(exchange, message: AbstractIncomingMessage) -> None:
    try:
        async with message.process(requeue=False):
            assert message.reply_to is not None

            n = int(message.body.decode())

            print(f" [.] fib({n})")
            print(f" [.] {message}")
            response = str(await asyncio.to_thread(fib, n)).encode()

            await exchange.publish(
                Message(
                    body=response,
                    correlation_id=message.correlation_id,
                ),
                routing_key=message.reply_to,
            )
            print("Request complete")
    except Exception:
        logging.exception("Processing error for message %r", message)



async def main() -> None:
    # Perform connection
    connection = await connect("amqp://guest:guest@localhost/")

    # Creating a channel
    channel = await connection.channel()
    exchange = channel.default_exchange

    # Declaring queue
    queue = await channel.declare_queue("rpc_queue")

    on_call = get_on_call(exchange)

    print(" [x] Awaiting RPC requests")

    await queue.consume(on_call)

    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
