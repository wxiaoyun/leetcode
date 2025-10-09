from typing import List

# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        total_t = 0
        # potion_t[i] = time taken to brew ith potion
        potion_t = [0] * n

        for ma in mana:
            new_potion_t = [0] * n
            slack = 0

            for i in reversed(range(n)):
                wiz = skill[i]
                t = ma * wiz
                new_potion_t[i] = t

                previous_t = potion_t[i + 1] if i < n - 1 else 0
                delta = t - previous_t - slack

                if delta > 0:
                    total_t += delta
                    slack = 0
                else:
                    slack = abs(delta)

            potion_t = new_potion_t

        return total_t
