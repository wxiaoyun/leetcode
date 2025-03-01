from typing import List

# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        # Set all negative values to 0 since they are irrelevant
        for i in range(N):
            nums[i] = max(nums[i], 0)
        
        # For each positive element k, we signal that k is present by
        # setting (k-1) th element as negative without changing its absolute value
        for i in range(N):
            k_minus_1 = abs(nums[i]) - 1
            # Verify k is positive and between 1 to N
            if k_minus_1 < 0 or k_minus_1 >= N:
                # In an array of length N, we can at most cover up to N from 1.
                # Any value above this range is irrelevant
                continue
            if nums[k_minus_1] > 0:
                # We mark k as present
                nums[k_minus_1] = -nums[k_minus_1]
            if nums[k_minus_1] == 0:
                # 0 is a neutral number
                # We set (k-1)th element to a large negative value
                # If we set nums[k_minus_1] to a value m smaller than (N+1), we might 
                # mislead the algorithm into thinking that m exists when it may not.
                nums[k_minus_1] = -(N+1) # Any value larger than N+1 will work

        # Find the first index, l = k-1, that has a positive element.
        # A positive element indictes that k is not yet seen. This is our result
        for i in range(N):
            if nums[i] >= 0:
                # (k-1) = i, k = i + 1
                return i + 1
        return N+1