import time
import gc

class DummyClass:
    def __init__(self, number):
        self.foo = [[] for _ in range(number)]

def generate_objects(number, size) -> None:
    bar = [DummyClass(size) for _ in range(number)]

# Allocate mass instances once
def test():
    times = []
    for _ in range(500):
        start_time = time.time()
        generate_objects(10000, 4)
        times.append(time.time() - start_time)

    avg_elapsed_time = sum(times) / len(times) * 1000
    max_elapsed_time = max(times) * 1000

    print(f"test: avg time: {avg_elapsed_time:.2f}ms, max time: {max_elapsed_time:.2f}ms")

# Allocate few instances but repeatedly
def test2():
    times = []
    for _ in range(500):
        start_time = time.time()
        for _ in range(100):
            generate_objects(100, 4)
        times.append(time.time() - start_time)

    avg_elapsed_time = sum(times) / len(times) * 1000
    max_elapsed_time = max(times) * 1000

    print(f"test2: avg time: {avg_elapsed_time:.2f}ms, max time: {max_elapsed_time:.2f}ms")

default_threshold = gc.get_threshold()


gc.disable()
print("threshold: disable")
test()
gc.enable()
gc.collect()
time.sleep(0.5)

gc.set_threshold(*default_threshold)
print("threshold: ", gc.get_threshold())
test()
gc.collect()
time.sleep(0.5)

gc.set_threshold(default_threshold[0], 999999999, 999999999)
print("threshold: ", gc.get_threshold())
test()
gc.collect()
time.sleep(0.5)


gc.set_threshold(default_threshold[0], 0, 999999999)
print("threshold: ", gc.get_threshold())
test()
gc.collect()
time.sleep(0.5)


gc.set_threshold(default_threshold[0], 0, 0)
print("threshold: ", gc.get_threshold())
test()
gc.collect()
time.sleep(0.5)

print()

gc.disable()
print("threshold: disable")
test2()
gc.enable()
gc.collect()
time.sleep(0.5)

gc.set_threshold(*default_threshold)
print("threshold: ", gc.get_threshold())
test2()
gc.collect()
time.sleep(0.5)

gc.set_threshold(default_threshold[0], 999999999, 999999999)
print("threshold: ", gc.get_threshold())
test2()
gc.collect()
time.sleep(0.5)


gc.set_threshold(default_threshold[0], 0, 999999999)
print("threshold: ", gc.get_threshold())
test2()
gc.collect()
time.sleep(0.5)


gc.set_threshold(default_threshold[0], 0, 0)
print("threshold: ", gc.get_threshold())
test2()
gc.collect()
time.sleep(0.5)
