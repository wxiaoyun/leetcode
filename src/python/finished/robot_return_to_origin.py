# https://leetcode.com/problems/robot-return-to-origin/


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counts = [0] * 4
        index = {
            "U": 0,
            "D": 1,
            "L": 2,
            "R": 3,
        }

        for mv in moves:
            counts[index[mv]] += 1

        return (abs(counts[0] - counts[1]) + abs(counts[2] - counts[3])) == 0
