from typing import List

# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        prev_even = [-1] * n
        prev_zero = [-1] * n
        prev_odd = [-1] * n
        prev_even[0] = 1

        for r in range(m):
            cur_even = [-1] * n
            cur_zero = [-1] * n
            cur_odd = [-1] * n

            for c in range(n):
                cur_val = grid[r][c]
                cur_val_abs = abs(cur_val)

                if cur_val > 0:
                    if c > 0 and cur_even[c - 1] > 0:
                        cur_even[c] = max(
                            cur_even[c],
                            cur_val_abs * cur_even[c - 1],
                        )
                    if prev_even[c] > 0:
                        cur_even[c] = max(cur_even[c], cur_val_abs * prev_even[c])

                    if c > 0 and cur_odd[c - 1] > 0:
                        cur_odd[c] = max(cur_odd[c], cur_val_abs * cur_odd[c - 1])
                    if prev_odd[c] > 0:
                        cur_odd[c] = max(cur_odd[c], cur_val_abs * prev_odd[c])

                elif cur_val < 0:
                    if c > 0 and cur_even[c - 1] > 0:
                        cur_odd[c] = max(
                            cur_odd[c],
                            cur_val_abs * cur_even[c - 1],
                        )
                    if prev_even[c] > 0:
                        cur_odd[c] = max(cur_odd[c], cur_val_abs * prev_even[c])

                    if c > 0 and cur_odd[c - 1] > 0:
                        cur_even[c] = max(
                            cur_even[c],
                            cur_val_abs * cur_odd[c - 1],
                        )
                    if prev_odd[c] > 0:
                        cur_even[c] = max(cur_even[c], cur_val_abs * prev_odd[c])

                else:  # cur_val == 0
                    cur_zero[c] = 0

                if prev_zero[c] == 0 or (cur_zero[c - 1] if c > 0 else -1) == 0:
                    cur_zero[c] = 0

            prev_even, prev_zero, prev_odd = cur_even, cur_zero, cur_odd
            # print(r)
            # print("E", prev_even)
            # print("O", prev_odd)
            # print()

        ans = max(prev_even[-1], prev_zero[-1])
        if ans < 0:
            return ans
        return ans % (int(1e9) + 7)
