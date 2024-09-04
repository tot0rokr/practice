# Process간 통신에 있어서 데이터를 전송할 때 pickle을 이용해 직렬화를 수행한다.
# 이 때, 분산 작업으로 인한 처리 시간 감소보다 데이터 전송에 필요한 직/역직렬화에
# 필요한 시간이 더 클 수 있다.
import asyncio
import multiprocessing
import random
import time
from typing import List
import gc

def generate_random_vector(size: int) -> List[float]:
    return [random.random() for _ in range(size)]

def element_wise_sum(vectors: List[List[float]]) -> List[float]:
    ret_vector = [0.0] * len(vectors[0])
    for vector in vectors:
        for i in range(len(vector)):
            ret_vector[i] += vector[i]
    return ret_vector

process_pool = multiprocessing.Pool(4)

async def multiprocess() -> List[float]:
    vectors = [generate_random_vector(512) for _ in range(100)]

    start_time = time.time()
    result_vector_list = process_pool.map(element_wise_sum, [
        vectors[:25], vectors[25:50], vectors[50:75], vectors[75:],
    ])
    ret_vector = element_wise_sum(result_vector_list)

    elapsed_time = time.time() - start_time
    print(f"multiprocess elapsed time: {elapsed_time * 1000:.1f}ms")
    return ret_vector

async def singleprocess() -> List[float]:
    vectors = [generate_random_vector(512) for _ in range(100)]

    start_time = time.time()
    ret_vector = element_wise_sum(vectors)

    elapsed_time = time.time() - start_time
    print(f"singleprocess elapsed time: {elapsed_time * 1000:.1f}ms")
    return ret_vector


def main():
    asyncio.run(multiprocess())
    gc.collect()
    asyncio.run(singleprocess())

if __name__ == "__main__":
    main()
