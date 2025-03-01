from typing import Optional

# https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        used = [False] * 10

        def compute(i: int, cur: list) -> Optional[str]:
            if i >= N:
                return "".join([str(ch) for ch in cur])
            
            inc = pattern[i] == "I"
            for n in range(1, 10):
                if used[n]:
                    continue
                if inc and cur[-1] >= n:
                    continue
                if not inc and cur[-1] <= n:
                    continue
                
                cur.append(n)
                used[n] = True
                res = compute(i + 1, cur)
                if res:
                    return res
                used[n] = False
                cur.pop()
            return None

        for n in range(1, 10):
            used[n] = True
            res = compute(0, [n])
            if res:
                return res
            used[n] = False
        return ""