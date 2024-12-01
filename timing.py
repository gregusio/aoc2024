from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time()
        res = f(*args, **kwargs)
        end_time = time()
        print(f'Elapsed time: {end_time - start_time} sec')
        return res
    
    return wrapper