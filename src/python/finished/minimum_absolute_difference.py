from typing import List

# https://leetcode.com/problems/minimum-absolute-difference/


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        pairs = []
        min_pair = 1 << 31

        arr = sorted(arr)
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < min_pair:
                pairs.clear()
                min_pair = diff

            if not pairs or diff == min_pair:
                pairs.append([arr[i - 1], arr[i]])

        return pairs
