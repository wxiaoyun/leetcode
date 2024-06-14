# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0]

        for n in arr:
            prefix_xor.append(n^prefix_xor[-1])
        
        total = 0
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if not prefix_xor[j+1] ^ prefix_xor[i]:
                    total += j-i
        return total
        
        