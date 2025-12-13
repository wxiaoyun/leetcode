from collections import deque
from typing import List

# https://leetcode.com/problems/course-schedule-ii/


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # number of courses that each course depends on
        dep_cnt = [0] * numCourses
        # adjacency list for the dependent nodes for each node
        adj_list = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj_list[b].append(a)
            dep_cnt[a] += 1

        leaf_nodes = deque()
        for i, cnt in enumerate(dep_cnt):
            if cnt == 0:
                leaf_nodes.append(i)

        ordering = []
        while leaf_nodes:
            i = leaf_nodes.popleft()
            ordering.append(i)

            for dependent in adj_list[i]:
                dep_cnt[dependent] -= 1
                if dep_cnt[dependent] == 0:
                    leaf_nodes.append(dependent)

        return ordering if len(ordering) == numCourses else []
