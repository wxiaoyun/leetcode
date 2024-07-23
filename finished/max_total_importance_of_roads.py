# https://leetcode.com/problems/maximum-total-importance-of-roads/

from collections import defaultdict
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cntRef = defaultdict(int)

        for city_a, city_b in roads:
            cntRef[city_a] += 1
            cntRef[city_b] += 1
        
        # city to importance dict

        city_tmp = [(cnt, city) for city, cnt in cntRef.items()]
        # print(city_tmp)

        # heapq.heapify(city_tmp)

        city_tmp.sort(key=lambda x: -x[0])
        # print(city_tmp)

        city_to_val = {}
        for idx, (_, city) in enumerate(city_tmp):
            value = n-idx
            city_to_val[city] = value
        # print(city_to_val)

        res = 0
        for city_a, city_b in roads:
            res += city_to_val[city_a]
            res += city_to_val[city_b]
        return res