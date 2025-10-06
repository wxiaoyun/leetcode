from typing import List

# https://leetcode.com/problems/zero-array-transformation-ii


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)
        prefix_mod = [0] * (n + 1)

        i = 0
        k = 0
        cur_mod = 0
        while i < n:
            cur_num = nums[i]
            cur_mod += prefix_mod[i]

            while cur_num > cur_mod and k < q:
                l, r, val = queries[k]

                if r < i:
                    k += 1
                    continue

                if l <= i:
                    cur_mod += val
                else:
                    prefix_mod[l] += val

                prefix_mod[r + 1] -= val
                k += 1

            if cur_num > cur_mod:
                return -1

            i += 1

        return k


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)

        delta = [0] * (N + 1)
        q = 0
        for i, n in enumerate(nums):
            while delta[i] < n:
                if q >= len(queries):
                    return -1

                l, r, v = queries[q]
                q += 1
                if r < i:
                    continue

                delta[max(i, l)] += v
                delta[r + 1] -= v

            delta[i + 1] += delta[i]

        return q
