# Find the Maximum Number in an Array
# Traverse the array and find the largest number.
# Input: [3, 7, 2, 9, 5]
# Expected Output: 9

inp = [3, 7, 2, 9, 5]
res = 0

for val in inp:
    if res < val:
        res = val

print(res)

