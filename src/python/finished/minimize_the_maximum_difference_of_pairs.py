# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def is_possible(nums: List[int], p: int, target: int) -> bool:
            i = 0
            count = 0
            while i < len(nums) - 1:
                a = nums[i]
                b = nums[i + 1]
                if b - a > target:
                    i += 1
                    continue
                count += 1
                i += 2
                if count >= p:
                    return True

            return count >= p

        nums = sorted(nums)
        ans = -1
        l, r = 0, nums[-1] - nums[0] + 1
        while l < r:
            m = l + (r - l) // 2

            if is_possible(nums, p, m):
                ans = m
                r = m
            else:
                l = m + 1
        return ans
