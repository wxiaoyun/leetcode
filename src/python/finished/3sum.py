from typing import List
from collections import Counter
import bisect

# https://leetcode.com/problems/3sum/


# O(n^2) time, O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums = sorted(nums)
        cnt = Counter(nums)

        for i in range(n):
            cnt[nums[i]] -= 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                cnt[nums[j]] -= 1
                target = -(nums[i] + nums[j])
                if target in cnt and cnt[target] > 0:
                    tmp = sorted([nums[i], nums[j], target])
                    res.add((tmp[0], tmp[1], tmp[2]))
            for j in range(i + 1, n):
                cnt[nums[j]] += 1

        return list(res)

# O(n^2 log n) time
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                target = -(nums[i] + nums[j])
                k = bisect.bisect_left(nums, target, lo = j + 1)
                if k < n and nums[k] == target:
                    tmp = sorted([nums[i], nums[j], nums[k]])
                    res.add((tmp[0], tmp[1], tmp[2]))
        return list(res)

# O(n^3) time
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return list(res)
