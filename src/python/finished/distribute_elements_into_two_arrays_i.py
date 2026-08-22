from typing import List

# https://leetcode.com/problems/distribute-elements-into-two-arrays-i


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1, a2 = [nums[0]], [nums[1]]

        for n in nums[2:]:
            if a1[-1] > a2[-1]:
                a1.append(n)
            else:
                a2.append(n)

        result = []
        result.extend(a1)
        result.extend(a2)
        return result
