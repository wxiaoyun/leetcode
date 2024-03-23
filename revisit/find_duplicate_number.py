# https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

            if fast == slow:
                break
        
        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]

            if slow == slow_2:
                return slow
