# 1. Timing Decorator
# Create a decorator that prints how long a function takes to run.

# import time
# def funcTimeCal(ref):
#     startTime = time.time()
#     def proceedDef():
#         time.sleep(2)
#         endTime = time.time()
#         excuTim = endTime - startTime
#         return f'{ref()} {excuTim:.4f} Seconds'
#     return proceedDef
    
# @funcTimeCal
# def myFunc():
#     return "Execution time is"

# print(myFunc())

import time
from functools import wraps

def TimiDecor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time.time()
        result = func(*args, **kwargs)
        endTime = time.time()
        execuTime = endTime - startTime
        print(f"Execution time: {execuTime:.4f} seconds")
        return result
    return wrapper

@TimiDecor
def myFun():
    time.sleep(2)
    return "Execution complete"

print(myFun())