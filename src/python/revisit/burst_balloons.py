from typing import List


# O(n^3)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def compute(dp: dict, nums: List[int], l: int, r: int) -> int:
            if l == r:
                return 0

            key = (l, r)
            if key in dp:
                return dp[key]

            best = 0
            for m in range(l, r):
                # pop m last

                # best for nums[l:m]
                left_best = compute(dp, nums, l, m)
                # best for nums[m+1:r]
                right_best = compute(dp, nums, m + 1, r)

                left = nums[l - 1] if l > 0 else 1
                right = nums[r] if r < len(nums) else 1
                best = max(best, left_best + left * nums[m] * right + right_best)
            dp[key] = best
            return best

        return compute({}, nums, 0, len(nums))


# O(2^n * n) TLE
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def compute(dp: dict, nums: List[int], kill: List[bool]) -> int:
            key = ".".join(str(n) for i, n in enumerate(nums) if not kill[i])
            if key in dp:
                return dp[key]

            n = len(nums)
            best = 0

            rem_nums = []
            for i in range(n):
                if kill[i]:
                    continue
                rem_nums.append(i)

            for j, i in enumerate(rem_nums):
                el = nums[i]
                prev = nums[rem_nums[j - 1]] if j > 0 else 1
                nxt = nums[rem_nums[j + 1]] if j + 1 < len(rem_nums) else 1

                kill[i] = True
                best = max(best, prev * el * nxt + compute(dp, nums, kill))
                kill[i] = False

            dp[key] = best
            return best

        return compute({}, nums, [False] * len(nums))
