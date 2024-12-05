from collections import deque

# https://leetcode.com/problems/move-pieces-to-obtain-a-string/

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        qs = deque()
        for i, c in enumerate(start):
          if c == "_":
            continue
          qs.append((i, c))

        qt = deque()
        for i, c in enumerate(target):
          if c == "_":
            continue
          qt.append((i, c))
        
        if len(qs) != len(qt):
          return False # impossible to match

        for i in range(len(qs)):
          si, sc = qs.popleft()
          ti, tc = qt.popleft()

          if sc != tc:
            return False
          
          if sc == "L" and si < ti: # start L cannot be on the left of target
            return False
          
          if sc == "R" and si > ti: # start R cannot be on the right of target
            return False

        return True