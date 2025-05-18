# 1. Log Function Calls
# Create a decorator @log_calls that prints:
# Function name
# Arguments
# Return value

import time

def log_calls(fn):
    def wrapper(*args, **kwargs):
        print(f"{fn.__name__} function is processing")
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__} function takes {end-start:.4f} seconds.")
    return wrapper

@log_calls()
def add(a, b):
    time.sleep(2)
    return a+b

@log_calls
def sub(a, b):
    return a-b

add(10,10)
sub(10, 5)

