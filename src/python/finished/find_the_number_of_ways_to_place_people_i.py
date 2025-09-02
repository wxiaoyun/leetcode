# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/


from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        pairs = 0

        for pi in points:
            xi, yi = pi

            for pj in points:
                if pi == pj:
                    continue

                xj, yj = pj
                if not (xi >= xj and yi <= yj):
                    continue

                rule_two_violated = False
                for pk in points:
                    if pk in [pi, pj]:
                        continue

                    xk, yk = pk
                    if (xj <= xk and xk <= xi) and (yi <= yk and yk <= yj):
                        rule_two_violated = True
                        break

                if not rule_two_violated:
                    pairs += 1

        return pairs
