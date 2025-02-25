from typing import List

# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum

class Solution:
    # Space optimized
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = 10**9 + 7
        even_count = 0
        odd_count = 0
        total = 0

        for i in range(N):
            n = arr[i]
            if n % 2 == 0:  # is even
                even_count = (even_count + 1) % MOD
            else:  # is odd
                tmp = odd_count
                odd_count = (1 + even_count) % MOD
                even_count = tmp

            total = (total + odd_count) % MOD

        return total


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = 10**9 + 7
        end_even = [0] * N
        end_odd = [0] * N

        total = 0
        if arr[0] % 2 == 0:
            end_even[0] = 1
        else:
            total = 1
            end_odd[0] = 1

        for i in range(1, N):
            n = arr[i]
            if n % 2 == 0:  # is even
                end_even[i] = 1
                end_even[i] = (end_even[i] + end_even[i - 1]) % MOD
                end_odd[i] = (end_odd[i] + end_odd[i - 1]) % MOD
            else:  # is odd
                end_odd[i] = 1
                end_odd[i] = (end_odd[i] + end_even[i - 1]) % MOD
                end_even[i] = (end_even[i] + end_odd[i - 1]) % MOD
            total = (total + end_odd[i]) % MOD

        return total
