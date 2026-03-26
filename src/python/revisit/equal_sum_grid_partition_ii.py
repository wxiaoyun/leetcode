from collections import Counter


class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        def check_section(target, r1, r2, c1, c2, counts):
            """Checks if target exists and keeps the rectangle [r1..r2, c1..c2] connected."""
            if target <= 0 or counts[target] == 0:
                return False
            h, w = r2 - r1 + 1, c2 - c1 + 1
            if h == 1 and w == 1:
                return False  # Sum becomes 0, never matches
            if h == 1:
                return grid[r1][c1] == target or grid[r1][c2] == target
            if w == 1:
                return grid[r1][c1] == target or grid[r2][c1] == target
            return True  # h > 1 and w > 1: any cell works

        # --- Horizontal Cuts ---
        row_sums = [sum(row) for row in grid]
        top_sum = 0
        top_counts = Counter()
        bot_counts = Counter()
        for r in range(m):
            for c in range(n):
                bot_counts[grid[r][c]] += 1

        for r in range(m - 1):  # Cut after row r
            top_sum += row_sums[r]
            for c in range(n):
                val = grid[r][c]
                top_counts[val] += 1
                bot_counts[val] -= 1

            bot_sum = total_sum - top_sum
            diff = top_sum - bot_sum
            if diff == 0:
                return True
            if diff > 0 and check_section(diff, 0, r, 0, n - 1, top_counts):
                return True
            if diff < 0 and check_section(-diff, r + 1, m - 1, 0, n - 1, bot_counts):
                return True

        # --- Vertical Cuts ---
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]
        left_sum = 0
        left_counts = Counter()
        right_counts = Counter()
        for r in range(m):
            for c in range(n):
                right_counts[grid[r][c]] += 1

        for c in range(n - 1):  # Cut after column c
            left_sum += col_sums[c]
            for r in range(m):
                val = grid[r][c]
                left_counts[val] += 1
                right_counts[val] -= 1

            right_sum = total_sum - left_sum
            diff = left_sum - right_sum
            if diff == 0:
                return True
            if diff > 0 and check_section(diff, 0, m - 1, 0, c, left_counts):
                return True
            if diff < 0 and check_section(-diff, 0, m - 1, c + 1, n - 1, right_counts):
                return True

        return False
