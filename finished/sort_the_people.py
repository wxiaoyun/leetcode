# https://leetcode.com/problems/sort-the-people

from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
      htp = {heights[i]:names[i] for i in range(len(names))}
      heights.sort(key=lambda x:-x)
      return [htp[h] for h in heights]
        