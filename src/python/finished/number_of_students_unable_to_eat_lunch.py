from typing import List

# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # [1,1,1]
        # [0,1,1]

        zeros = students.count(0)
        ones = len(students) - zeros
        cnt = [zeros, ones]

        for i, sw in enumerate(sandwiches):
            if cnt[sw] == 0:
                return len(sandwiches) - i
            cnt[sw] -= 1
        return 0
