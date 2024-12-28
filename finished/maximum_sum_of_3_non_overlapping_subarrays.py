from typing import Dict, List, Tuple

# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)

        prefix_sum = [0]
        for i in range(N):
            prefix_sum.append(nums[i] + prefix_sum[-1])

        # array sum from i to j exclusive: [i, j)
        def subarr_sum(i: int, k: int) -> int:
            return prefix_sum[i + k] - prefix_sum[i]

        def compute(times: int, prev: Dict[int, Tuple[int, list]] = None):
            if times == 0:
                return prev

            if not prev:
                prev = {i: (0, []) for i in range(N + k + 1)}

            dp: Dict[int, Tuple[int, list]] = {}
            for i in reversed(range(N - k + 1)):
                prev_idx = i + k
                if prev_idx not in prev:
                    continue

                ps, pls = prev[i + k]
                s = ps
                s += subarr_sum(i, k)
                ls = pls[:]
                ls.append(i)

                if i + 1 in dp:
                    ps, pls = dp[i + 1]
                    if ps > s:
                        s = ps
                        ls = pls

                dp[i] = (s, ls)

            return compute(times - 1, dp)

        res = compute(3)
        res = res[0][1]
        res.reverse()
        return res
