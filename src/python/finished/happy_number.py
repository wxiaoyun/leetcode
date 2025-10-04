# https://leetcode.com/problems/happy-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        cur = n
        seen = set()
        while cur not in seen:
            seen.add(cur)
            if cur == 1:
                return True

            new_cur = 0
            while cur != 0:
                digit = cur % 10
                cur = cur // 10
                new_cur += digit * digit

            cur = new_cur

        return False
