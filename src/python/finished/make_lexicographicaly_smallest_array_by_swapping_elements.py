from typing import List

# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = [(n, i) for i, n in enumerate(nums)]
        pairs.sort()

        groups = []
        grp = []
        for pair in pairs:
            if not grp:
                grp.append(pair)
                continue
            
            if pair[0] - grp[-1][0] <= limit:
                grp.append(pair)
                continue
            
            groups.append(grp)
            grp = [pair]
        if grp:
            groups.append(grp)

        res = [0] * len(nums)
        for grp in groups:
            indices = [i for _, i in grp]
            indices.sort()

            for i, (n, _) in enumerate(grp):
                index = indices[i]
                res[index] = n

        return res