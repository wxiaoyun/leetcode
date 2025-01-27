from typing import List

# https://leetcode.com/problems/course-schedule-iv

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        N = numCourses
        prq = [[] for _ in range(N)]

        for a, b in prerequisites:
            prq[b].append(a)

        cache = {}
        def is_prq(a: int, b: int) -> bool:
            key = (a, b)
            if key in cache:
                return cache[key]

            for pre in prq[b]:
                if pre == a or is_prq(a, pre):
                    cache[key] = True
                    return True
            
            cache[key] = False
            return False
        
        return [is_prq(a, b) for a, b in queries]
  
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        N = numCourses

        mat = [[float('inf')] * N for _ in range(N)]
        for a, b in prerequisites:
            mat[a][b] = 1

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    mat[i][j] = min(
                        mat[i][j],
                        mat[i][k] + mat[k][j]
                    )
        
        return [mat[a][b] < float('inf') for a, b in queries]

