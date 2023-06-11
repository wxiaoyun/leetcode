from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        count = 0
        # invariant: nums[0:count] are all unique elements at the end of every iteration
        for i in range(0, len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1 # plus one since count is an index