# https://neetcode.io/problems/non-cyclical-number/


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        cur = n
        while cur not in seen:
            if cur == 1:
                return True
            seen.add(cur)

            local_sum = 0
            tmp = cur
            while tmp != 0:
                local_sum += (tmp % 10) ** 2
                tmp = tmp // 10
            cur = local_sum

        return False
