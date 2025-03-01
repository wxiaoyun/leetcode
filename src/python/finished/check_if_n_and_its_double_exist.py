from typing import List

# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
          if n/2 in seen or 2*n in seen:
            return True
          seen.add(n)
        return False