# 2. Call-Counting Decorator
# Write a decorator that tracks how many times a function has been called.
# After calls, you should be able to access the call count via function_name.
# call_count.

call_count = {}

def callCnt(fn):
    def wrapper():
        if call_count:
            call_count['count'] += 1
        else:
            call_count['count'] = 1
        return fn(call_count['count'])
    return wrapper

@callCnt
def count_the_call(cnt):
    print(f'Counting: {cnt}')

count_the_call()
count_the_call()
count_the_call()
print(call_count['count'])