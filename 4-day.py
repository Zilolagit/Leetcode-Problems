"""
LeetCode Problem

Theme: Python
Difficulty: Easy
Solutions: 1
Link: https://leetcode.com/problems/valid-parentheses/

"""


from typing import List

# First Way

def isValid(s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack


result = isValid("([])")

print(result)

