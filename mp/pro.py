"""
multiprocess will execute multiple tasks at a time

"""
from time import perf_counter
from functools import wraps
from datetime import datetime


def get_time(func):
    @wraps(func)
    def wapper(*args, **kwargs):
        s = perf_counter()
        func(*args, **kwargs)
        e = perf_counter()
        print(f'time: {e - s} seconds')

    return wapper


def timestamp() -> str:
    return f'{datetime.now():%H%M%S}'
