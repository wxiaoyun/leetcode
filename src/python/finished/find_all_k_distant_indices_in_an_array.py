from typing import List

# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        last_added = -1
        deez = []
        for i, n in enumerate(nums):
            if n != key:
                continue

            for j in range(max(last_added + 1, i - k), min(N, i + k + 1)):
                deez.append(j)
                last_added = j

        return deez
