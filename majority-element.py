# QUESTION: Level of Interview Question = Easy
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Example 1:
# Input: [3,2,3]
# Output: 3
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

# çözüm:1
for i in Input:
    if Input.count(i) > len(Input) / 2:
        print(i)
        break

# çözüm:2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = set(nums)
        for i in x:
            if nums.count(i) > len(nums)/2:
                return i

#çözüm:3
def majorityElement(nums):
    return max(set(nums),key=nums.count)