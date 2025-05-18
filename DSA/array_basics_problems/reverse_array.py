# Reverse an Array
# Input: [1, 2, 3, 4, 5]
# Expected Output: [5, 4, 3, 2, 1]

inp = [1,2,3,4,5]
rever_inp = []

for i, val in enumerate(inp):
    rever_inp.append(inp[len(inp)-i-1])

print(rever_inp)