from typing import List

# https://leetcode.com/problems/partition-array-according-to-given-pivot

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        p_count = 0

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                p_count += 1
            else:
                more.append(n)
        
        res = less + [pivot] * p_count
        res.extend(more)
        return res