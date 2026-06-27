from collections import Counter
from typing import List

# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ks = sorted(list(cnt.keys()))
        best = 0
        for v in ks:
            cur = v
            l = 0
            while cur in cnt and cnt[cur] >= 2:
                l += 2
                cnt[cur] -= 2
                cur = cur * cur
            if cur in cnt and cnt[cur] == 1:
                l += 1
                cnt[cur] -= 1
            else:
                l -= 1
                cnt[cur] += 1
            best = max(best, l)
            # print(v, l, best)

        return best
