from typing import List

# https://leetcode.com/problems/greatest-sum-divisible-by-three/


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        min_mod = [float("inf")] * 3
        min_mod[0] = 0
        total = 0
        for n in nums:
            total += n
            i = n % 3
            for j in range(3):
                if j == i:
                    continue
                k = (j - i) % 3
                min_mod[j] = min(min_mod[j], min_mod[k] + n)
            min_mod[i] = min(min_mod[i], n)
        return total - min_mod[total % 3]
