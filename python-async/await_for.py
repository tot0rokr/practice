import asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(1)
    print('yay!')
    return True

async def main():
    # Wait for at most 1 second
    try:
        print(await asyncio.wait_for(eternity(), timeout=2.0))
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
