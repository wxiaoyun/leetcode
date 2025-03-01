from typing import List

# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums = sorted(nums)

        res = []
        def helper(i: int, arr: List[int]) -> None:
            if i >= N:
                res.append(arr)
                return None
            
            # Take
            helper(i+1, arr+[nums[i]])
            # No take
            j = i + 1
            while j < N and nums[j] == nums[i]:
                j += 1
            helper(j, arr)
            return None
        helper(0, [])
        return res