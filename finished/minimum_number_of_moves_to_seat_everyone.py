# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone

from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        output = 0
        for i in range(len(seats)):
            output += abs(seats[i]-students[i])
        return output
        