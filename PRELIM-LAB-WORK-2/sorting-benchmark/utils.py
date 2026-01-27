import random
import time


def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def time_sort(sort_function, data):
    start = time.perf_counter()
    result = sort_function(data)
    end = time.perf_counter()
    return result, end - start
