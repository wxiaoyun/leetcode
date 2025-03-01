# https://leetcode.com/problems/single-number-iii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dif = 0
        for n in nums:
            dif ^= n
        
        dif_bit_index = -1
        dif_bin = format(dif, '032b')

        for i in range(len(dif_bin)):
            b = dif_bin[i]
            if b == '1':
                dif_bit_index = i
                break
        

        num_a, num_b = 0, 0

        for n in nums:
            n_bin = format(n, '032b')

            if n_bin[dif_bit_index] == '0':
                num_a ^= n
            else:
                num_b ^= n

        return [num_a, num_b]