from collections import defaultdict
from typing import List

# https://leetcode.com/problems/pyramid-transition-matrix


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        blocks = defaultdict(set)
        for blk in allowed:
            assert len(blk) == 3
            blocks[blk[:2]].add(blk[2])

        def dfs(bottom: List[str], idx: int, builder: List[str]) -> bool:
            if idx >= len(builder):
                if len(builder) == 1:
                    return True
                return dfs(builder, 0, [""] * (len(builder) - 1))

            assert len(bottom) == len(builder) + 1

            blk = bottom[idx] + bottom[idx + 1]

            if blk not in blocks:
                return False

            for opt in blocks[blk]:
                prev = builder[idx]
                builder[idx] = opt
                if dfs(bottom, idx + 1, builder):
                    return True
                builder[idx] = prev

            return False

        return dfs(list(bottom), 0, [""] * (len(bottom) - 1))
