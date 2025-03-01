from typing import List

# https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = [s[:spaces[0]]]

        for i in range(len(spaces)-1):
          res.append(s[spaces[i]: spaces[i+1]])

        res.append(s[spaces[-1]:])
        return " ".join(res)