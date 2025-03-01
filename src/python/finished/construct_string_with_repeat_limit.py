from collections import Counter
import heapq

# https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ctr = Counter(s)

        res = []
        pq = [(-ord(ch), cnt) for ch, cnt in ctr.items()]
        heapq.heapify(pq)
        NULL = (float('inf'), 0)
        prev = NULL
        while pq:
          ch_ord, cnt = heapq.heappop(pq)
          taken = 0

          if prev[0] < ch_ord: # if prev is lexicographically larger
            taken = 1
            res.append(chr(-ch_ord))
          else:
            taken = min(repeatLimit, cnt)
            res.append(chr(-ch_ord) * taken)
          cnt -= taken

          if prev != NULL:
            heapq.heappush(pq, prev)
            
          if cnt == 0:
            prev = NULL
          else:
            prev = (ch_ord, cnt)

        return "".join(res)

