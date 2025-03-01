# https://leetcode.com/problems/sum-of-digits-of-string-after-convert

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        new_s = []
        for c in s:
            new_s.append(str(ord(c)-ord('a')+1))
        new_s = "".join(new_s)
        
        res = new_s
        for _ in range(k):
            tmp = 0
            for c in res:
                tmp += int(c)
            res = str(tmp)
        return int(res)