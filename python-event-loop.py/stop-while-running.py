import signal
import asyncio
from functools import partial

async def sub_job():
  print("sub_job")

async def job(loop):
  print("job1")
  #  loop.call_soon(signal.raise_signal, signal.SIGINT)
  signal.raise_signal(signal.SIGINT)
  print("job2")

def sig_handler(loop):
  print("sig handler")
  loop.create_task(sub_job())
  loop.stop()

loop = asyncio.get_event_loop()
loop.add_signal_handler(signal.SIGINT, partial(sig_handler, loop))
loop.create_task(job(loop))
print("running")
loop.run_forever()
loop.close()
