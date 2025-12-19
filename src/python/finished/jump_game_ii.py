from collections import deque
from typing import List

# https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque([0])
        steps = [float("inf")] * n
        it = 0
        while q:
            l = len(q)
            for _ in range(l):
                idx = q.popleft()

                if steps[idx] <= it:
                    continue
                steps[idx] = it

                for j in range(idx + 1, min(n, idx + nums[idx] + 1)):
                    q.append(j)
            it += 1
        return steps[-1]
