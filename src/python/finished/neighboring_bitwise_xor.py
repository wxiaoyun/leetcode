from typing import List

# https://leetcode.com/problems/neighboring-bitwise-xor/description/

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        def check(initial: int) -> bool:
            def helper(i: int, prev: int) -> bool:
                if i == len(derived):
                    return prev

                target = derived[i]
                nxt = target ^ prev
                return helper(i+1, nxt)
            return initial == helper(0, initial)
        return check(0) or check(1)