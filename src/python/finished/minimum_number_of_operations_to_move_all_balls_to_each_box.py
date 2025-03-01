from typing import List

# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)

        lballs = 0
        rballs = 0
        lcost = 0
        rcost = 0
        ans = [0] * N

        for i in range(N):
          j = N - 1 - i
          ans[i] += lcost
          ans[j] += rcost
          
          b = boxes[i]
          if b == '1':
            lballs += 1
          lcost += lballs

          b = boxes[j]
          if b == '1':
            rballs += 1
          rcost += rballs

        return ans
      
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)

        lcost = [(0, 0)]
        for b in boxes:
          cost, num = lcost[-1]
          if b == '1':
            num += 1
          lcost.append((cost + num, num))

        rcost = [(0, 0)]
        for b in reversed(boxes):
          cost, num = rcost[-1]
          if b == '1':
            num += 1
          rcost.append((cost + num, num))

        res = []
        for i in range(N):
          lc, _ = lcost[i]
          rc, _ = rcost[N-1-i]
          res.append(lc + rc)
        return res