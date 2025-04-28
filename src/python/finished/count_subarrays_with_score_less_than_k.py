from typing import List

# https://leetcode.com/problems/count-subarrays-with-score-less-than-k


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        psum = [0]  # psum[i] == sum(nums[:i])

        def bsearch(psum: List[int], k: int) -> int:
            arr_len = len(psum) - 1
            l, r = 0, arr_len
            res = arr_len
            total = psum[-1]

            while l < r:
                m = l + (r - l) // 2

                msum = psum[m]  # sum from 0 to m (exclusive)
                interval_sum = total - msum  # sum from m onwards
                interval_len = arr_len - m
                score = interval_sum * interval_len

                if score < k:
                    res = m
                    r = m
                else:
                    l = m + 1
            return res

        count = 0
        for r, n in enumerate(nums):
            psum.append(psum[-1] + n)
            count += r - bsearch(psum, k) + 1

        return count
