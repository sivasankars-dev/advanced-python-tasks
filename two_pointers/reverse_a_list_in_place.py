# 🔹 2. Reverse a List In-Place
# Problem:
# Reverse the given array in-place (without using extra space).
# Input:
arr = [5, 10, 15, 20]
# Expected Output:
# [20, 15, 10, 5]

for val in range(len(arr)//2):
    arr[val], arr[len(arr)-val-1] = arr[len(arr)-val-1], arr[val]

