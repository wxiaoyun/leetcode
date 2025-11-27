from typing import List

# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        bests = [-float('inf')] * k
        best = -float('inf')
        acc = 0
        for i, n in enumerate(nums):
            acc += n
            if i >= k:
                acc -= nums[i - k]
            if i >= k - 1 :
                j = i % k
                bests[j] = max(bests[j] + acc, acc)
                best = max(best, bests[j])
        return best