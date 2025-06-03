"""
LeetCode Problem

Theme: Python
Difficulty: Easy
Solutions: 1
Link: https://leetcode.com/problems/palindrome-number/description/

"""


from typing import List

# First Way

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

result = isPalindrome(10)

print(result)