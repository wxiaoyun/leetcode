from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[a].append(b)

        dp = {}

        def can_finish(course: int) -> bool:
            # can_finish(course) iff
            # for all course' in prerequisites[course], can_finish(course)

            if course in dp:
                return dp[course]

            dp[course] = False
            for dep in adj_list[course]:
                if not can_finish(dep):
                    return False
            dp[course] = True
            return True

        return all(can_finish(course) for course in range(numCourses))
