# https://leetcode.com/problems/palindrome-partitioning/

from collections import deque
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_pldm(s: str) -> bool:
            mid = len(s) // 2
            for i in range(mid+1):
                j = len(s)-1-i
                if not s[i] == s[j]:
                    return False
            return True
        
        out = []
        unique = set()
        queue = deque()
        queue.append([c for c in s])

        while len(queue) > 0:
            p = queue.popleft()
            p_str = str(p)
            if p_str in unique:
                continue
            unique.add(p_str)
            out.append(p)

            for i in range(len(p)):
                if i+1 < len(p):
                    l, r = p[i], p[i+1]
                    merged = l+r
                    if is_pldm(merged):
                        new_p = []
                        new_p.extend(p[:i])
                        new_p.append(merged)
                        new_p.extend(p[i+2:])
                        queue.append(new_p)
                    
                if i+2 < len(p):
                    l, m, r = p[i], p[i+1], p[i+2]
                    merged = l+m+r
                    if is_pldm(merged):
                        new_p = []
                        new_p.extend(p[:i])
                        new_p.append(merged)
                        new_p.extend(p[i+3:])
                        queue.append(new_p)
        
        return [item for item in out]