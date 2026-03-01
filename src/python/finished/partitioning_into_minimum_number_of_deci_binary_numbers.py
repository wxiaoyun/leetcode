# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers


class Solution:
    def minPartitions(self, n: str) -> int:
        return max((int(d) for d in n), default=0)
