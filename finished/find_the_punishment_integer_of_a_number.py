from collections import defaultdict

# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        cache = defaultdict(dict)
        def check(sq: int, n: int) -> bool:
            if sq in cache[n]:
                return cache[n][sq]

            if sq == n:
                return True
            
            if n <= 0 or sq < n:
                return False

            res = False
            pw = 10
            while pw <= 1000:
                if check(sq // pw, n - (sq % pw)):
                    res = True
                    break
                
                pw *= 10

            cache[n][sq] = res
            return res
        
        p = 0
        for i in range(n):
            j = i + 1
            sq = j ** 2
            p += sq if check(sq, j) else 0
        return p

    def punishmentNumber(self, n: int) -> int:
        cache = defaultdict(dict)
        def check(target: int, rem: str) -> bool:
            rem_or_zero = rem or "0"
            rem_num = int(rem_or_zero)
            if target in cache[rem_num]:
                return cache[rem_num][target]


            if target == 0 and rem_num == 0:
                return True
            
            if target == 0 or rem_num == 0:
                return False

            res = False
            for i in range(1, len(rem)+1):
                sub = int(rem[:i])

                if target >= sub and check(target - sub, rem[i:]):
                    res = True
                    break

            cache[rem_num][target] = res
            return res

        def is_punishable(n: int) -> bool:
            squared = n ** 2
            sstr = str(squared)
            punishable = check(n, sstr)
            return punishable
        
        p = 0
        for i in range(n):
            j = i + 1
            p += j ** 2 if is_punishable(j) else 0
        return p