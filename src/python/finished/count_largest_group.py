from collections import Counter

# https://leetcode.com/problems/count-largest-group


class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = Counter()
        for i in range(1, n + 1):
            sm = sum([int(d) for d in str(i)])
            cnt[sm] += 1

        mx = max(cnt.values())
        res = 0
        for v in cnt.values():
            res += 1 if v == mx else 0
        return res
