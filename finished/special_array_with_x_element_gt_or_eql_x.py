# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # def partition(i: int, j: int):
        #     if i >= j:
        #         return
            
        #     p = nums[i]
        #     nums[i], nums[j] = nums[j], nums[i]

        #     k = i
        #     while k < j:
        #         if nums[k] < p:
        #             nums[i], nums[k] = nums[k], nums[i]
        #             i+=1
        #         k+=1
        #     nums[i], nums[j] = nums[j], nums[i]
        #     return i

        # def qsort(i: int, j: int):
        #     if i >= j:
        #         return
            
        #     mid = partition(i, j)
        #     qsort(i, mid-1)
        #     qsort(mid+1, j)

        # qsort(0, len(nums)-1)
        nums.sort()

        for i in range(len(nums)):
            l = nums[i-1] if i > 0 else -float('inf')
            r = nums[i]
            target = len(nums)-i

            if l < target and target <= r:
                return target
        return -1

        