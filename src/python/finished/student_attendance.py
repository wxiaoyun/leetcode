# https://leetcode.com/problems/student-attendance-record-i/

class Solution:
    def checkRecord(self, s: str) -> bool:
        def helper(i: int, nlate: int, nabs: int) -> bool:
            if i >= len(s):
                return True
            
            is_late = s[i] == 'L'
            is_abs = s[i] == 'A'
            is_pre = s[i] == 'P'
            
            if is_late:
                nlate+=1
                if nlate >= 3:
                    return False
            
            if is_abs:
                nabs+=1
                nlate=0
                if nabs >= 2:
                    return False
            
            if is_pre:
                nlate=0
            
            return helper(i+1, nlate, nabs)

        return helper(0, 0, 0)