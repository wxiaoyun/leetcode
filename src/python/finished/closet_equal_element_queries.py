from collections import defaultdict
from typing import List

# https://leetcode.com/problems/closest-equal-element-queries


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        rev_index = defaultdict(list)

        for i, num in enumerate(nums):
            rev_index[num].append(i)
        # print(rev_index)

        res = []
        for i in queries:
            target = nums[i]

            search_list = rev_index[target]

            if len(search_list) <= 1:
                res.append(-1)
                continue

            l, r = 0, len(search_list)
            search_list_index = -1
            while l < r:
                m = l + (r - l) // 2
                j = search_list[m]

                if j <= i:
                    search_list_index = m
                    l = m + 1
                else:
                    r = m

            # print(i, nums[i], search_list_index)

            INF = 1 << 32
            best = INF

            l_index = (search_list_index - 1) % len(search_list)
            r_index = (search_list_index + 1) % len(search_list)

            best = min(
                best, abs(search_list[l_index] - i), n - abs(search_list[l_index] - i)
            )
            # print("l", best)
            best = min(
                best, abs(search_list[r_index] - i), n - abs(search_list[r_index] - i)
            )
            # print("r", best)

            res.append(best)

        return res
