import heapq
from typing import List

# https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    # Time: O(max(n, m))
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
      jobs = [0 for _ in range(len(s)+1)]
      for start, end, d in shifts:
        delta = d if d > 0 else -1
        jobs[start] += delta
        jobs[end+1] -= delta

      res = []
      delta = 0
      for i, ch in enumerate(s):
        delta += jobs[i]
        
        ch_int = (ord(ch) - ord('a') + delta) % 26 + ord('a')
        res.append(chr(ch_int))

      return "".join(res)
  
    # Time: O(max(n, m))
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        jobs = [[] for _ in range(len(s) + 1)]
        for start, end, d in shifts:
            delta = d if d > 0 else -1
            jobs[start].append(delta)
            jobs[end + 1].append(-delta)

        res = []
        delta = 0
        for i, ch in enumerate(s):
            for jb in jobs[i]:
                delta += jb

            ch_int = (ord(ch) - ord("a") + delta) % 26 + ord("a")
            res.append(chr(ch_int))

        return "".join(res)

    # Time: O(nlogm)
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_level = [[] for _ in s]
        for sh in shifts:
            start = sh[0]
            shift_level[start].append(sh)

        delta = 0
        pq = []
        res = []
        for i, ch in enumerate(s):
            while pq and pq[0][0] < i:
                _, d = heapq.heappop(pq)
                delta -= d

            for _, end, d in shift_level[i]:
                d = d if d > 0 else -1
                delta += d
                heapq.heappush(pq, (end, d))

            ch_int = (ord(ch) - ord("a") + delta) % 26 + ord("a")
            res.append(chr(ch_int))

        return "".join(res)

    # Time: O(nm), m is the length of shifts
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        res = [ord(s[i]) - ord("a") for i in range(len(s))]

        for s, e, d in shifts:
            if d == 0:
                d = -1

            for j in range(s, e + 1):
                res[j] += d
                res[j] %= 26

        return "".join([chr(ch + ord("a")) for ch in res])
