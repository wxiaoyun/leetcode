from typing import List

# https://leetcode.com/problems/remove-methods-from-project/


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        adj_list = [[] for _ in range(n)]
        in_deg = [0] * n
        for caller, callee in invocations:
            adj_list[caller].append(callee)
            in_deg[callee] += 1

        non_sus = set(range(n))
        sus = [k]
        visited = [False] * n
        while sus:
            meth = sus.pop()
            if visited[meth]:
                continue
            # print(meth)
            visited[meth] = True
            non_sus.remove(meth)

            for callee in adj_list[meth]:
                sus.append(callee)
                # remove all sus incoming edges
                in_deg[callee] -= 1

        for meth in range(n):
            if meth in non_sus:
                continue
            # sus method
            if in_deg[meth] > 0:
                # this sus method cannot be removed
                return list(range(n))

        return list(non_sus)
