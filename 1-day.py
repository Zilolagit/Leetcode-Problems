"""
LeetCode Problem

Theme: Python
Difficulty: Easy
Solutions: 2
Link: https://leetcode.com/problems/two-sum/description/?search=python

"""


from typing import List

# First Way
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Second Way (Optimal)

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for index, value in enumerate(nums):
        difference = target - value
        if difference in num_dict:
            return [num_dict[difference], index]
        num_dict[value] = index

result = twoSum([7, 1, 5, 4, 1], 5)
print(result)