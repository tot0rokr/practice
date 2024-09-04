import asyncio

async def sub_job():
  print("sub_job")

async def job():
  print("job1")
  await asyncio.sleep(0)
  await sub_job()
  print("job2")

def main(loop):
  print("main1")
  loop.create_task(job())
  loop.stop()
  print("main2")

loop = asyncio.get_event_loop()
main(loop)
loop.run_forever()
loop.close()
