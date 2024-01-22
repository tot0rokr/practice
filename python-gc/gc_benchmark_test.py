import time
import gc

class DummyClass:
    def __init__(self):
        self.foo = [[] for _ in range(4)]

def generate_objects() -> None:
    bar = [DummyClass() for _ in range(10000)]

def test():
    times = []
    for _ in range(500):
        start_time = time.time()
        generate_objects()
        times.append(time.time() - start_time)

    avg_elapsed_time = sum(times) / len(times) * 1000
    max_elapsed_time = max(times) * 1000

    print(f"avg time: {avg_elapsed_time:.2f}ms, max time: {max_elapsed_time:.2f}ms")

default_threshold = gc.get_threshold()


gc.disable()
print("disable")
test()
gc.enable()
gc.collect()

print("threshold: ", gc.get_threshold())
test()
gc.collect()

gc.set_threshold(default_threshold[0], 999999999, 999999999)
print("threshold: ", gc.get_threshold())
test()
gc.collect()


gc.set_threshold(default_threshold[0], 0, 999999999)
print("threshold: ", gc.get_threshold())
test()
gc.collect()


gc.set_threshold(default_threshold[0], 0, 0)
print("threshold: ", gc.get_threshold())
test()
gc.collect()
