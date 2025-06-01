# https://leetcode.com/problems/distribute-candies-among-children-ii


class Solution:
      def distributeCandies(self, n: int, limit: int) -> int:
        def n_choose_2(n: int) -> int:
            if n < 2:
                return 0
            return n * (n - 1) // 2

        # n!/k!(n - k)!
        
        # _, _, _, _ // (n + 2) locations, choose 2 location to put "iron bar" to distribute

        total_ways = n_choose_2(n + 2)
        one_child_extra = 3 * n_choose_2(n + 2 - (limit + 1))
        two_child_extra = 3 * n_choose_2(n + 2 - (limit + 1) * 2)
        three_child_extra = n_choose_2(n + 2 - (limit + 1) * 3)
        return total_ways - one_child_extra + two_child_extra - three_child_extra
  
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, limit) + 1):
            irem = n - i
            if irem > limit * 2:
                continue

            end = min(irem, limit)  # the second child cannot take more than limit
            start = max(0, irem - limit)  # the last child cannot take more than limit

            combination = end - start + 1
            res += combination

        return res

    # TLE
    def distributeCandies(self, n: int, limit: int) -> int:
        # T(n, limit, group) = Sum i from 0 to limit (
        #  T(n - i, limit, group - 1)
        # )

        # Base cases:
        # T(n, limit, 1) = 0 if n > limit
        # T(n, limit, 1) = 1 if n <= limit
        # T(n, limit, group) = 0 if n < 0

        def compute(dp: dict, n: int, limit: int, group: int) -> int:
            if n < 0:
                return 0
            if group == 1:
                if n > limit:
                    return 0
                return 1

            key = (n, group)
            if key in dp:
                return dp[key]

            res = 0
            for i in range(limit + 1):
                res += compute(dp, n - i, limit, group - 1)

            dp[key] = res
            return res

        dp = {}
        return compute(dp, n, limit, 3)
