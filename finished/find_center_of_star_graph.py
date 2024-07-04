# https://leetcode.com/problems/find-center-of-star-graph

from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # cnt = defaultdict(int)

        # for u, v in edges:
        #     cnt[u]+=1
        #     cnt[v]+=1
        
        # for key, val in cnt.items():
        #     if val > 1:
        #         return key
        
        cnt = defaultdict(int)

        for u, v in edges:
            cnt[u]+=1
            cnt[v]+=1
            if cnt[u] > 1:
                return u
            if cnt[v] > 1:
                return v