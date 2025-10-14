from typing import List

# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/


# O(n), single pass
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prevl = 0
        l = 1
        for i in range(1, len(nums) + 1):
            prev = nums[i - 1]
            cur = nums[i] if i < len(nums) else -1001

            if cur > prev:
                l += 1
            else:
                if l >= 2 * k:
                    return True
                if prevl >= k and l >= k:
                    return True
                prevl, l = l, 1

        return False


# O(n), two passes
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        inc_arrs = []

        l = 1
        for i in range(1, len(nums) + 1):
            prev = nums[i - 1]
            cur = nums[i] if i < len(nums) else -1001

            if cur > prev:
                l += 1
            else:
                if l >= 2 * k:
                    return True
                inc_arrs.append(l)
                l = 1

        for j in range(1, len(inc_arrs)):
            if inc_arrs[j - 1] >= k and inc_arrs[j] >= k:
                return True
        return False
