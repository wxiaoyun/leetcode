# https://leetcode.com/problems/campus-bikes-ii/


from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        ALL_ALLOCATED_MASK = (1 << len(workers)) - 1

        dp = {}

        def compute(bk_idx: int = 0, worker_rem: int = 0) -> int:
            key = (bk_idx, worker_rem)
            if key in dp:
                return dp[key]

            if worker_rem == ALL_ALLOCATED_MASK:
                return 0

            if bk_idx >= len(bikes):
                return float("inf")

            # for each bike, there is k + 1 choices
            # k: we can allocate it to one of the remaining k workers
            # 1: or skip it

            # skip current bike and do not assign to anyone
            best = compute(bk_idx + 1, worker_rem)

            bikex, bikey = bikes[bk_idx]
            # try allocating the bike to each remaining worker
            for i in range(len(workers)):
                is_worker_allocated = ((worker_rem >> i)) & 1 == 1
                if is_worker_allocated:
                    continue

                workerx, workery = workers[i]
                worker_bike_dist = abs(bikex - workerx) + abs(bikey - workery)

                new_worker_rem = worker_rem | (1 << i)
                best = min(best, worker_bike_dist + compute(bk_idx + 1, new_worker_rem))

            dp[key] = best
            return best

        return compute()
