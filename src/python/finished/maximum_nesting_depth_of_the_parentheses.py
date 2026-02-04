# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/


class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth, cur_depth = 0, 0
        for ch in s:
            if ch == "(":
                cur_depth += 1
            elif ch == ")":
                cur_depth -= 1
            max_depth = max(max_depth, cur_depth)
        return max_depth
