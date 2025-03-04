# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 12 // 3 = 4 R 0
        # 4 // 3 = 1 R 1
        # 1 // 3 = 0 R 1

        # 21 // 3 = 7 R 0
        # 7 // 3 = 2 R 1
        # 2 // 3 = 0 R 2

        cur = n
        while cur:
            rem = cur % 3
            if rem == 2:
                return False
            cur = cur // 3
        return True
