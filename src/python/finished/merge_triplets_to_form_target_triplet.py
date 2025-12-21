from typing import List

# https://leetcode.com/problems/merge-triplets-to-form-target-triplet


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ta, tb, tc = target

        aa, bb, cc = 0, 0, 0
        for a, b, c in triplets:
            if a > ta or b > tb or c > tc:
                continue
            if a == ta or b == tb or c == tc:
                aa = max(a, aa)
                bb = max(b, bb)
                cc = max(c, cc)

        return aa == ta and bb == tb and cc == tc
