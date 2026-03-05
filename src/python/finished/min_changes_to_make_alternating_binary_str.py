# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/


class Solution:
    def minOperations(self, s: str) -> int:
        def make(s: str, i: int, is_zero: bool) -> int:
            changes = 0
            while i < len(s):
                target = "0" if is_zero else "1"
                if s[i] != target:
                    changes += 1

                i += 1
                is_zero = not is_zero
            return changes

        return min(make(s, 0, True), make(s, 0, False))


class Solution:
    def minOperations(self, s: str) -> int:
        def helper(s: str, i: int, c: str, accum: int) -> int:
            if i >= len(s):
                return accum

            next_c = "0" if c == "1" else "1"

            if s[i] != c:
                return helper(s, i + 1, next_c, accum + 1)
            else:
                return helper(s, i + 1, next_c, accum)

        return min(helper(s, 0, "1", 0), helper(s, 0, "0", 0))
