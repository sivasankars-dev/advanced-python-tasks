def closureCall(fn):
    cnt = 0
    def wrapper(num):
        nonlocal cnt
        cnt += num
        return fn(cnt)
    
    def reset():
        nonlocal cnt
        cnt = 0

    wrapper.reset = reset
    return wrapper

@closureCall
def callFn(val):
    print(val)

callFn(9)
callFn(1)
callFn.reset()
callFn(5)