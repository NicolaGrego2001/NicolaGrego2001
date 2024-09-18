from functools import wraps
from time import perf_counter, sleep


def timing_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = f(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print(f"Function {f.__name__} took {execution_time:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def funzione_da_cronometrare(s):
    sleep(s)
    return 'Done'

result = funzione_da_cronometrare(2)
print(result)