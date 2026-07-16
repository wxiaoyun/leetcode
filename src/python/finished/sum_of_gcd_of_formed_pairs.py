from math import gcd

# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = 0
        gcds = [-1] * n
        for i, n in enumerate(nums):
            mx = max(mx, n)
            gcds[i] = gcd(mx, n)
        gcds.sort()

        ans = 0
        for i in range(len(gcds) // 2):
            ans += gcd(gcds[i], gcds[len(gcds) - 1 - i])
        return ans
