from typing import List

# https://leetcode.com/problems/minimum-absolute-difference/


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        pairs = []

        arr = sorted(arr)
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if pairs and diff < (pairs[-1][1] - pairs[-1][0]):
                pairs = []

            if not pairs or diff == (pairs[-1][1] - pairs[-1][0]):
                pairs.append([arr[i - 1], arr[i]])

        return pairs
