from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time()
        res = f(*args, **kwargs)
        end_time = time()
        print(f'Elapsed time: {round((end_time - start_time) * 1000, 2)} ms')
        return res
    
    return wrapper