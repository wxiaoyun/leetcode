from collections import deque
from typing import List

# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        def can_complete(
            tasks: List[int],
            workers: List[int],
            total_pills: int,
            strength: int,
            k: int,
        ) -> bool:
            rem_pills = total_pills
            taskq = deque()
            t_ptr = 0

            for w in workers[-k:]:
                while t_ptr < k and tasks[t_ptr] <= w + strength:
                    taskq.append(tasks[t_ptr])
                    t_ptr += 1

                if not taskq:
                    return False

                if taskq[0] <= w:
                    taskq.popleft()
                    continue

                if rem_pills == 0:
                    return False

                rem_pills -= 1
                taskq.pop()

            return True

        tasks = sorted(tasks)
        workers = sorted(workers)

        l, r = 0, min(len(tasks), len(workers)) + 1
        res = 0
        while l < r:
            m = l + (r - l) // 2
            print(l, m, r)
            if can_complete(tasks, workers, pills, strength, m):
                res = m
                l = m + 1
            else:
                r = m
        return res
