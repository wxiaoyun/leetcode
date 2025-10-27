from typing import List


# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_device_cnt = 0
        beams = 0
        for row in bank:
            device_cnt = row.count("1")
            if device_cnt == 0:
                continue

            beams += device_cnt * prev_device_cnt
            prev_device_cnt = device_cnt

        return beams
