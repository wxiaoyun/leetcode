from typing import List


# https://leetcode.com/problems/sum-of-distances
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def helper(nums: List[int]) -> List[int]:
            N = len(nums)
            ans = [0] * N
            prefix_count = {}
            prefix_offset = {}
            for i in range(N):
                n = nums[i]

                cur_sum = prefix_count.setdefault(n, 0) * i - prefix_offset.setdefault(
                    n, 0
                )
                ans[i] = cur_sum

                prefix_count[n] += 1
                prefix_offset[n] += i

            return ans

        ans = helper(nums)
        rev_ans = helper(list(reversed(nums)))

        for i, n in enumerate(rev_ans):
            ans[len(nums) - 1 - i] += n
        return ans
