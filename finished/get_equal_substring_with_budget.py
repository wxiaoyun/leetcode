# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def cost(s: int, t: int) -> int:
            return abs(ord(s)-ord(t))
        
        _max = 0
        cur_cost = 0
        l = 0

        for r in range(len(s)):
            cur_cost += cost(s[r], t[r])

            while cur_cost > maxCost:
                cur_cost -= cost(s[l], t[l])
                l+=1
            
            _max = max(_max, r-l+1)
        
        return _max