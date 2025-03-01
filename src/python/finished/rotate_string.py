from collections import Counter

# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
          return False
        
        if Counter(s) != Counter(goal):
          return False

        n = len(goal)
        for i in range(n):
          found_invalid = False
          for j in range(n):
            k = (i + j) % n
            if goal[j] != s[k]:
              found_invalid = True
              break
          
          if not found_invalid:
            return True
        return False
        