# https://leetcode.com/problems/1-bit-and-2-bit-characters/

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < (n - 1):
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2

        return i == n - 1
