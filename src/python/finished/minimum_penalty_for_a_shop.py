# https://leetcode.com/problems/minimum-penalty-for-a-shop


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Before closing:
        # Y: 0, N: 1
        # After closing:
        # Y: 1, N: 0

        # We minimise cost before closing by reducing the number of "N"
        # We minimise cost after closing by reducing number of "Y"

        # Suppose we move forward the closing hour by 1 and customer did arrive in the previous hour:
        # .......YH.........
        # BC penalty: +0
        # AC penalty: +1
        #
        # Suppose we move forward the closing hour by 1 and customer did NOT arrive in the previous hour:
        # .......NH.........
        # BC penalty: -1
        # AC penalty: +0

        # prefix_sum[i] = count of "Y" in customers[0:i]
        prefix_sum = [0]
        for ch in customers:
            prefix_sum.append(prefix_sum[-1])
            if ch == "Y":
                prefix_sum[-1] += 1

        n = len(customers)
        best = n
        best_hr = -1
        for i in range(n + 1):
            bc_penalty = i - prefix_sum[i]
            ac_penalty = prefix_sum[-1] - prefix_sum[i]
            cur_penalty = bc_penalty + ac_penalty
            if cur_penalty < best:
                best = bc_penalty + ac_penalty
                best_hr = i

        return best_hr
