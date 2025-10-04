# https://leetcode.com/problems/container-with-most-water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1

        max_amt = 0
        while l < r:
            lh = height[l]
            rh = height[r]

            h = min(lh, rh)
            b = r - l
            max_amt = max(max_amt, b * h)

            if lh < rh:
                l += 1
            else:
                r -= 1

        return max_amt
