# Build a Custom Flask-like Route Decorator
# @route("/home")
# def home():
#     return "Welcome!"
import sys
# li = [num for num in range(10000000)]
# print(sys.getsizeof(li))
ge = (num for num in range(10000000))
print(sys.getsizeof(ge), next(ge), next(ge))
