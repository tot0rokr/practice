from multiprocessing import Process
import time


def hello():
    time.sleep(5)

p = Process(target=hello)
p.start()

while p.is_alive():
    print("is alive")
    time.sleep(0.5)

p.join()
