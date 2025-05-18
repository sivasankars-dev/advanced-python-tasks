# Find the Index of an Element
# Input: Array = [5, 10, 15, 20], Element to find = 15
# Expected Output: 2
# (Because indexing usually starts from 0)

arr = [5,10,15,20]
find = 15
for i, val in enumerate(arr):
    if find == val:
        print(f"Expected index of {val} is {i}") 