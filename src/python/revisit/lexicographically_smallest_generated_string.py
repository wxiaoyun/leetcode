# https://leetcode.com/problems/lexicographically-smallest-generated-string/


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        WILDCARD = "."
        ans = [WILDCARD] * (n + m - 1)

        for i in range(n):
            if str1[i] == "F":
                continue

            for j in range(m):
                if ans[i + j] != WILDCARD and ans[i + j] != str2[j]:
                    return ""
                ans[i + j] = str2[j]

        for i in range(n):
            if str1[i] == "T":
                continue

            if any(
                (ans[i + j] if ans[i + j] != WILDCARD else "a") != str2[j]
                for j in range(m)
            ):
                continue

            unequal = False
            for j in reversed(range(m)):
                if ans[i + j] == WILDCARD:
                    ans[i + j] = "b"
                    unequal = True
                    break

            if not unequal:
                return ""

        for i in range(len(ans)):
            if ans[i] == WILDCARD:
                ans[i] = "a"
        return "".join(ans)
