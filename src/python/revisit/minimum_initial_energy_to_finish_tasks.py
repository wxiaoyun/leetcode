from typing import List

# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # If I have x energy, then any task of cost y, min_en z, where x >= y >= z, such that is essentially "free"
        # Doing this task will not cause any previously available task to become unavailable

        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)

        def possible(e: int) -> bool:
            for a, m in tasks:
                if m > e:
                    # our energy is non-increasing
                    # if we encounter an undoable task, we can never do it in the future
                    return False
                else:
                    e -= a
            return True

        l, r = max(m for a, m in tasks), sum(m for a, m in tasks) + 1
        ans = -1
        while l < r:
            m = l + (r - l) // 2
            # print(l, r)
            # print(m)
            if possible(m):
                ans = m
                r = m
            else:
                l = m + 1
        return ans
