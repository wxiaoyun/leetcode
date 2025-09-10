# https://leetcode.com/problems/minimum-number-of-people-to-teach/

from typing import List


class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        lang_set = [set(l) for l in languages]

        # Q1: how to efficiently tell there is a common language between 2 users

        # for each friendship, check for common language or learn the new language

        cache = {}

        def has_common_lang(u: int, v: int) -> bool:
            if u > v:
                u, v = v, u

            key = (u, v)
            if key in cache:
                return cache[key]

            common_lang = lang_set[u] & lang_set[v]
            res = len(common_lang) > 0
            cache[key] = res
            return res

        def guess(lang: int) -> int:
            new_learn = set()

            for u, v in friendships:
                u, v = u - 1, v - 1
                if has_common_lang(u, v):
                    continue

                if u not in new_learn and lang not in lang_set[u]:
                    new_learn.add(u)

                if v not in new_learn and lang not in lang_set[v]:
                    new_learn.add(v)

            return len(new_learn)

        return min(guess(l) for l in range(1, n + 1))
