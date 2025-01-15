# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits2 = 0

        # 110 = 6
        # 6 // 2 = 3 R 0
        # 3 // 2 = 1 R 1
        # 1 // 2 = 0 R 1
        while num2 > 0:
            rem = num2 % 2
            num2 = num2 // 2
            bits2 += rem

        bits1 = 0
        bin1 = [] # LSB to MSB
        while num1 > 0:
            rem = num1 % 2
            num1 = num1 // 2
            bin1.append(rem)
            bits1 += rem

        if bits2 <= bits1:
            res = 0
            bits = 0
            for i in reversed(range(len(bin1))):
                if bin1[i] == 1 and bits < bits2:
                    res += 1 << i
                    bits += 1
            return res
        
        # bits2 > bits1
        res = 0
        excess = bits2 - bits1
        for i, b in enumerate(bin1):
            if b == 1:
                res += 1 << i
                continue

            if excess > 0: # b == 0
                res += 1 << i
                excess -= 1

        digit = len(bin1)
        while excess > 0:
            res += 1 << digit
            digit += 1
            excess -= 1
        
        return res
