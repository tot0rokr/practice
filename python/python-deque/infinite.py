from collections import deque
import time
from typing import Deque


def roundrobin(*iterable):
    queue = deque(*iterable)
    while True:
        try:
            while True:
                yield queue[0]
                queue.rotate(-1)
        except IndexError:
            yield "NO"
            queue.extend("NO")
        except StopIteration:
            # Remove an exhausted iterator.
            queue.popleft()


for i in roundrobin():
    print(i)
    time.sleep(1)
