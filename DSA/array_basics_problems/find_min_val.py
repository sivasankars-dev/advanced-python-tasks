# Find the Minimum Number in an Array

# Input: [3, 7, 2, 9, 5]

# Expected Output: 2
inp = [3, 7, 2, 9, 5]
res = inp[0]

for i in inp[1:]:
    if i < res:
        res = i

print(res)