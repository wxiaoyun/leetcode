import heapq
from typing import Optional, Tuple

# https://leetcode.com/problems/longest-happy-string/

# # Intuition
# This solution can be generalized to any list of (character, count) pairs of length *p* and any maximum allowed repeat length *k*

# # Approach
# <!-- Describe your approach to solving the problem. -->

# # Complexity
# - Time complexity:
# O(l*log(p)), where l is the max result string length. Here l = a+b+c

# - Space complexity:
# O(p), where p is number of (char, count) pairs. In the context of this question, p = 3

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        k = 2
        pq = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(pq)

        res = []
        streak_char: Tuple[str, int] = ("", 0) # (char, streak_len)
        streak_pair: Optional[Tuple[int, str]] = None
        while pq: # O(a + b + c) iterations
          count, char = heapq.heappop(pq) # O(log(p))
          if count == 0:
            continue # do not add it back to heap
          
          # We can generalize k to any positive integer larger than 1
          if streak_char[0] == char and streak_char[1] == k:
            streak_pair = (count, char)
            continue
          
          res.append(char)
          # Update streak
          streak_char = (char, streak_char[1] + 1 if streak_char[0] == char else 1)
          
          count = -count
          count -= 1
          heapq.heappush(pq, (-count, char))
          if streak_pair and char != streak_pair[1]:
            heapq.heappush(pq, streak_pair)
            streak_pair = None

        return "".join(res)