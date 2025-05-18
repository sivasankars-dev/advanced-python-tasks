# Two Sum II – Input Array is Sorted
# Problem:
# Return the indices (0-based) of the two numbers that add up to the target.

# Input:
arr = [2, 3, 5, 7, 11]
target = 10

# Expected Output:
# [1, 3]

# (Because 3 + 7 = 10)

def findSum(inp, tar):
    left = 0
    right = len(arr)-1

    while left<right:
        res = inp[left]+inp[right]

        if res == tar:
            return [left, right]
        elif res < tar:
            left +=1
        else:
            right -=1
    
print(findSum(arr, target))