# https://leetcode.com/problems/largest-3-same-digit-number-in-string/


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""

        char = ""
        cnt = 0
        for ch in num:
            if ch != char:
                char = ch
                cnt = 1
                continue

            cnt += 1
            if cnt != 3:
                continue

            local = ch * 3
            if best == "":
                best = local
                continue

            best = max(best, local)

        return best
