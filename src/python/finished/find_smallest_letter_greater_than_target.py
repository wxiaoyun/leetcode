from typing import List

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters)
        ans = 0
        while l < r:
            m = l + (r - l) // 2
            if letters[m] <= target:
                l = m + 1
            else:
                ans = m
                r = m
        return letters[ans]
