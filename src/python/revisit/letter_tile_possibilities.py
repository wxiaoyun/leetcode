from collections import Counter
from typing import List

# https://leetcode.com/problems/letter-tile-possibilities

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        pos = set()

        def compute(cur: List[str]) -> None:
            cur_str = "".join(cur)
            pos.add(cur_str)

            for ch in cnt.keys():
                fq = cnt[ch]
                if fq == 0:
                    continue
                
                cnt[ch] -= 1
                cur.append(ch)
                compute(cur)
                cur.pop()
                cnt[ch] += 1
            
            return None
        
        compute([])
        return len(pos) - 1
