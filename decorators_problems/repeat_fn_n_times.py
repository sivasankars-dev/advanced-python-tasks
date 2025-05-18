def nTime(fn):
    def wrapper(val):
        fn(val)
    return wrapper

@nTime
def greet(n):
    for i in range(n):
        print("Hii")

@nTime
def wish(n):
    for i in range(n):
        print("hello!")

greet(3)
wish(5)