class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        reachable = [False] * n
        reachable[0] = True

        j = 0
        for i in range(n):
            if not reachable[i]:
                continue

            j = max(j, i + minJump)
            while j < min(i + maxJump + 1, n):
                if s[j] == "0":
                    reachable[j] = True
                j += 1

        return reachable[-1]
