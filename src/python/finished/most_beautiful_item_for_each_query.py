from param import List

# https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        q = [(cost, i) for i, cost in enumerate(queries)]
        q.sort()
        items.sort()

        ans = [0] * len(q)
        max_beauty = 0
        j = 0
        for cost, i in q:
            while j < len(items) and items[j][0] <= cost:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            ans[i] = max_beauty

        return ans