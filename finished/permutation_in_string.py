# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            if not s1[i] in s1_count:
                s1_count[s1[i]] = 0
            s1_count[s1[i]] += 1

            if not s2[i] in s2_count:
                s2_count[s2[i]] = 0
            s2_count[s2[i]] += 1
        
        for i in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            
            s2_count[s2[i - len(s1)]] -= 1
            if s2_count[s2[i - len(s1)]] == 0:
                del s2_count[s2[i - len(s1)]]

            if not s2[i] in s2_count:
                s2_count[s2[i]] = 0
            s2_count[s2[i]] += 1
        
        return s1_count == s2_count