from typing import List

# https://leetcode.com/problems/find-the-string-with-lcp


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        interference_graph = [[False] * (n + 1) for _ in range(n + 1)]
        share_graph = [[False] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                l = lcp[i][j]
                if lcp[i][j] != lcp[j][i]:
                    # print("asymmetric", i, j)
                    return ""
                if (
                    i > 0
                    and j > 0
                    and lcp[i - 1][j - 1] > 0
                    and lcp[i][j] != lcp[i - 1][j - 1] - 1
                ):
                    # print("prior mismatch", i, j)
                    return ""
                if (
                    i > 1
                    and lcp[i - 2][j] > 1
                    and lcp[i - 2][j] - 1 == lcp[i - 1][j]
                    and lcp[i - 1][j] - 1 != lcp[i][j]
                ):
                    # print('top mismatch', i, j)
                    return ""
                # if j > 1:
                #     print(i, j, lcp[i][j - 2],lcp[i][j - 1],lcp[i][j])
                if (
                    j > 1
                    and lcp[i][j - 2] > 1
                    and lcp[i][j - 2] - 1 == lcp[i][j - 1]
                    and lcp[i][j - 1] - 1 != lcp[i][j]
                ):
                    # print('left mismatch', i, j)
                    return ""
                share_graph[i][j] = l > 0
                share_graph[j][i] = l > 0

                a, b = i + l, j + l
                if a > n or b > n:
                    # print("too long", i, j)
                    return ""
                interference_graph[a][b] = True
                interference_graph[b][a] = True

        NIL = "."
        colors = list("abcdefghijklmnopqrstuvwxyz")
        ans = [NIL] * n

        for i in range(n):
            options = colors[:]
            share_set = set()

            # print(i, ans)
            # print("interference", interference_graph[i])
            # print("share", share_graph[i])

            for j in range(n):
                interferes = interference_graph[i][j]
                shares = share_graph[i][j]
                # print("j", j)
                if j > i:
                    break
                if not (interferes ^ shares):
                    return ""
                if not interferes:
                    assert shares
                    if ans[j] != NIL:
                        share_set.add(ans[j])
                    continue
                if interferes and j == i:
                    return ""

                jcolor = ans[j]
                assert jcolor != NIL
                options[ord(jcolor) - ord("a")] = NIL

            if len(share_set) > 1:
                # print("share_set larger than 1", share_set)
                return ""
            for color in options:
                if color != NIL:
                    ans[i] = color
                    break
            if ans[i] == NIL:
                # print("no color")
                return ""

            # print("left options", options)
            # print(i, ans)
            # print()

        return "".join(ans)
