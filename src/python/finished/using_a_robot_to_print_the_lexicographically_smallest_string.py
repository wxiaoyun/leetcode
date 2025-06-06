# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string


class Solution:
    def robotWithString(self, s: str) -> str:
        # for every character in s:
        # append to t:
        # - Choice 1: immediately add to p:
        # - Choice 2: wait and see if theres smaller character

        N = len(s)
        pos_min = [N - 1] * N
        for i in reversed(range(N - 1)):
            if s[pos_min[i + 1]] < s[i]:
                pos_min[i] = pos_min[i + 1]
            else:
                pos_min[i] = i

        t = []
        p = []
        for i, ch in enumerate(s):
            t.append(ch)

            while t and (i == N - 1 or (t[-1] <= s[pos_min[i + 1]])):
                p.append(t.pop())

        return "".join(p)
