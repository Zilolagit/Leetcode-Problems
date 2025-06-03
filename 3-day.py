"""
LeetCode Problem

Theme: Python
Difficulty: Easy
Solutions: 1
Link: https://leetcode.com/problems/longest-common-prefix/?search=python

"""


from typing import List

# First Way

def longestCommonPrefix( strs: List[str]) -> str:
    ans=""
    v=sorted(strs)
    print(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ans
        ans += first[i]
    return ans

result = longestCommonPrefix(["flower","flow","flight"])

print(result)