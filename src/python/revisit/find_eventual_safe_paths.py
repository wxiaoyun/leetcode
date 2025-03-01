from typing import List

# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        
        path = set()
        visited = set()
        def check_cycle(n: int) -> bool:
            if n in path:
                return True
            if n in visited:
                return False
            visited.add(n)
            
            path.add(n)
            for nb in graph[n]:
                if check_cycle(nb):
                    return True
            path.remove(n)
            return False
        
        for i in range(N):
            check_cycle(i)
        
        res = []
        for i in range(N):
            if i not in path:
                res.append(i)
        return res

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        
        visited = [False] * N
        path = [False] * N
        def check_cycle(n: int) -> bool:
            # print(path)
            if path[n]:
                return True
            if visited[n]:
                return False
            visited[n] = True

            path[n] = True
            for nb in graph[n]:
                if check_cycle(nb):
                    return True
            path[n] = False

            return False
        
        for i in range(N):
            check_cycle(i)
        
        res = []
        for i in range(N):
            if not path[i]:
                res.append(i)

        return res