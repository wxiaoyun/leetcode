# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        # invariant: min element is always between nums[l] and nums[r]
        while l <= r:
            # if nums[l] is smaller than nums[r] then nums[l] must be the smallest element
            if nums[l] <= nums[r]:
                return nums[l]

            # otherwise, there is a cliff between nums[l] and nums[r]
            mid = (r - l) // 2 + l

            if nums[l] <= nums[mid]:
                # there is no cliff between l and mid
                l = mid + 1
            else:
                r = mid

        return False
            

        
