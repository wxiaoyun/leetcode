# https://leetcode.com/problems/number-of-substrings-with-only-1s/


class Solution:
    def numSub(self, s: str) -> int:
        MOD = int(1e9 + 7)
        total = 0
        streak = 0
        for ch in s:
            if ch == "0":
                n_choose_two = (streak * (streak + 1) // 2) % MOD
                total = (total + n_choose_two) % MOD
                streak = 0
            elif ch == "1":
                streak += 1
        n_choose_two = (streak * (streak + 1) // 2) % MOD
        total = (total + n_choose_two) % MOD
        return total
