# QUESTION:
# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target. You may assume that each input would have exactly one solution, and you may
# not use the same element twice. You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9, Output: [0,1] Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6, Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6, Output: [0,1]

#çözüm 1:
def summ(nums, target):
    for i in nums:
        for j in [n for n in arr if n != i]:
            if i+j==target:
                return sorted([nums.index(i), nums.index(j)])

# Çözüm-2
def twoSum2(nums, target):
    return [[i] + [nums.index(target-nums[i])] for i in range(len(nums)) if (target-nums[i] in nums) and nums.index(target-nums[i]) != i][0]

# çözüm-3
def twoSum4(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]], i]
        d[nums[i]] = i

# Çözüm-4
def twoSum1(nums, target):
    for i in range(len(nums)):
        if (target-nums[i] in nums) and nums.index(target-nums[i]) != i:
            return [i, nums.index(target-nums[i])]