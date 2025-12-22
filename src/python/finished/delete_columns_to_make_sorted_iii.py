from typing import List

# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        # observation 1:
        # - if a string is already in lexicographic order, the string remains in order
        #   after any arbitrary indice deletion
        #   - A monotonic property

        # observation 2:
        # - The set of indices to delete will be monotonically increasing when we add
        #   more strings

        # observation 3:
        # Suppose we know the minimum deletion set for a string prefix. This set may not be
        # globally optimal:
        #
        # Given "wxyzabcdefg"
        # It is optimal to delete "a" for prefix "wxyza" to obtain "wxyz"
        # But the global optimal is to delete "wxyz" to obtain "abcdefg"

        # let dp[j] = maximum non-deleted set where column j is NOT deleted

        # dp[j] = max from 0..=j-1 (
        #   0 if strs[i][j - 1] > strs[i][j],
        #   dp[j - 1]
        # )

        dp = [1] * m

        for j in range(m):
            for jj in range(j):
                ok = True
                for i in range(n):
                    if strs[i][jj] > strs[i][j]:
                        ok = False
                        break

                if not ok:
                    continue

                dp[j] = max(dp[j], dp[jj] + 1)

        return m - max(dp)
