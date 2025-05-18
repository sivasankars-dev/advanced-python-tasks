# Count Even and Odd Numbers in an Array
# Input: [2, 3, 4, 5, 6]
# Expected Output:
# Evens = 3 (2, 4, 6)
# Odds = 2 (3, 5)

inp = [2, 3, 4, 5, 6]
even = 0
odd = 0
for val in inp:
    if val%2==0:
        even += 1
    else:
        odd += 1

print("even", even)
print("odd", odd)
print('hello siva')