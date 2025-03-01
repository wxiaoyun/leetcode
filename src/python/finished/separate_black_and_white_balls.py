from collections import deque

# https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        # swap until all zeros on the left and ones on the right
        # we keep track of indices of the zeros in a queue
        arr = [c for c in s]
        white = deque()
        for i, c in enumerate(s):
          if c == '0':
            white.append(i)
        
        swaps = 0
        for j in range(len(arr)):
          c = arr[j]
          if c != '1':
            continue # current char is zero. Nothing to be done.

          while white and white[0] <= j:
            white.popleft() # Ignore all zeros on the left
          if not white:
            return swaps
          
          i = white.popleft()
          swaps += i-j # swap one and zero
          arr[i] = '1'
        return swaps
