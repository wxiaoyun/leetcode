from collections import defaultdict

# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freq = defaultdict(int)
        last_seen = {}
        count = set()

        for i, ch in enumerate(s):
          freq[ch] += 1
          if freq[ch] == 3:
            count.add(ch * 3)

          if ch in last_seen:
            last_idx = last_seen[ch]
            
            for j in range(last_idx + 1, i):
              count.add(f"{ch}{s[j]}{ch}")
          
          last_seen[ch] = i
        
        return len(count)

          