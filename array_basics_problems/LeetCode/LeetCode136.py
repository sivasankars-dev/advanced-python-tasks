# LeetCode: 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# Our Solution:
# 1. Here we want to find the unique number which is not twise in the given array. it's related to subarray
#    problem. 
# 2. We will create first one empty dictionary and save to res variable.
# 3. iterate the loop upto length of given array minus one(len(arr)-1)
# 4. Then we are going to save each array value as key and that count.
# 5. after the iteration we want to check which key has 0 value from the saved dictionary
# 6. iterate again the dictnary and check value match with 0. If it's matching with 0 value then return the key

def singleNumber(nums):
    res = {}
    for i in range(len(nums)):
        if nums[i] in res:
            res[nums[i]] = 1
        else:
            res[nums[i]] = 0

    for key in res:
        if res[key] == 0:
            return key

print(singleNumber([4,1,2,1,2])) # output: 4
print(singleNumber([2,2,1])) # output 1
print(singleNumber([1])) # output 1
