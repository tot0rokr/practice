import random
#  import multiprocessing as mp
import concurrent.futures
import time

data = list()
is_thread = True
# is_thread = False
thread_num = 8

size = 1000000

for i in range(size):
    data.append(int(random.random() * size))

def merge_sort(arr, a, b, is_thread):
    global size
    nr_half = a + (b - a) // 2

    if is_thread and (b - a) > size // thread_num:
        is_thread = True
    else:
        is_thread = False

    if b - a > 2:
        if is_thread:
            pool = concurrent.futures.ProcessPoolExecutor(max_workers=2)
            arr1 = arr[:nr_half]
            arr2 = arr[nr_half:]
            p1 = pool.submit(merge_sort, *[arr1, 0, nr_half - a, is_thread])
            p2 = pool.submit(merge_sort, *[arr2, 0, b - nr_half, is_thread])
            procs = {p1: True, p2: False}

            for pp in concurrent.futures.as_completed(procs):
                if procs[pp]:
                    arr[a:nr_half] = pp.result()
                else:
                    arr[nr_half:b] = pp.result()

        else:
            arr[a:nr_half] = merge_sort(arr, a, nr_half, is_thread)
            arr[nr_half:b] = merge_sort(arr, nr_half, b, is_thread)
        sorted_arr = list()
        left = a
        right = nr_half
        for i in range(a, b):
            if right >= b:
                sorted_arr.append(arr[left])
                left += 1

            elif left >= nr_half:
                sorted_arr.append(arr[right])
                right += 1

            elif arr[left] > arr[right]:
                sorted_arr.append(arr[right])
                right += 1

            else:
                sorted_arr.append(arr[left])
                left += 1

    elif b - a == 2:
        if arr[a] > arr[b - 1]:
            arr[a], arr[b - 1] = arr[b - 1], arr[a]
        sorted_arr = arr[a:b]

    else:
        sorted_arr = [arr[a]]

    return sorted_arr

start_time = time.time()
merge_sort(data, 0, size, is_thread)
end_time = time.time()
print ("duration: {}, len: {}".format(end_time - start_time, len(data)))
print (data[:10], data[-10:])
