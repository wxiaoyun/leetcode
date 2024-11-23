from typing import List

# https://leetcode.com/problems/rotating-the-box/

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        R = len(box)
        C = len(box[0])

        for row in box:
          row.append('*')

        for r in range(R):
          for c in reversed(range(C+1)):
            if box[r][c] != '*':
              continue
            stone_count = 0
            for i in reversed(range(c)):
              if box[r][i] == '*':
                break
              if box[r][i] == '#':
                stone_count += 1
              box[r][i] = '.'
            for i in range(stone_count):
              box[r][c-1-i] = '#'
        
        res = []
        for c in range(C):
          res.append([])
          for r in range(R):
            res[-1].append(box[R-1-r][c])

        return res
        