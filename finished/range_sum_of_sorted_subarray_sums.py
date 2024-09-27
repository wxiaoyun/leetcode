# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums


from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        def generate_subarr_sum() -> List[int]:
            n = len(nums)
            result = []
            
            for i in range(n):
                current_sum = 0
                for j in range(i, n):
                    current_sum += nums[j]
                    result.append(current_sum)
            
            return result
            
        sum_list = generate_subarr_sum()
        sum_list.sort()
        return sum(sum_list[left-1:right]) % (10**9 + 7)