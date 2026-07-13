from typing import List

# https://leetcode.com/problems/rank-transform-of-an-array


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arri = list((n, i) for i, n in enumerate(arr))
        arri.sort()
        ans = [0] * len(arr)
        rank = 1
        if arr:
            ans[arri[0][1]] = rank
        for i in range(1, len(arr)):
            if arri[i - 1][0] != arri[i][0]:
                rank += 1
            j = arri[i][1]
            ans[j] = rank
        return ans
