# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution:
    def minSwaps(self, s: str) -> int:
        bcount = 0
        swaps = 0

        for c in s:
          if c == '[':
            bcount += 1
          else:
            if bcount == 0:
              bcount += 1
              swaps += 1
            else:
              bcount -= 1
        
        return swaps

# class Solution:
#     def minSwaps(self, s: str) -> int:
#         stack = []
#         count = 0

#         for b in s:
#           if b == "[":
#             stack.append(b)
#             continue
          
#           if not stack:
#             count += 1
#           else:
#             stack.pop()

#         if stack:
#           count += 1
        
#         return count // 2


# class Solution:
#     def minSwaps(self, s: str) -> int:
#       dp: Dict[Tuple[int, int], Optional[int]] = defaultdict(lambda: None)

#       def helper(i: int, count: int, flip: int) -> int:
#         if count < 0:
#           return float('inf')

#         key = (i, count)
#         if key in dp:
#           return dp[key]

#         if i == len(s):
#           if count != 0:
#             dp[key] = float('inf')
#           else:
#             dp[key] = flip
#           return dp[key]
        
#         lowest = float('inf')
#         if s[i] == "[":
#           lowest = min(lowest, helper(i+1, count+1, flip))
#           lowest = min(lowest, helper(i+1, count-1, flip+1))
#         elif s[i] == "]":
#           lowest = min(lowest, helper(i+1, count-1, flip))
#           lowest = min(lowest, helper(i+1, count+1, flip+1))
#         dp[key] = lowest
#         return lowest
      
#       return helper(0, 0, 0) // 2
        
