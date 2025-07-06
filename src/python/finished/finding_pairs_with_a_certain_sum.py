from collections import Counter
from typing import List

# https://leetcode.com/problems/finding-pairs-with-a-certain-sum


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.m1 = Counter(nums1)
        self.m2 = Counter(nums2)
        self.m2_index = {i: v for i, v in enumerate(nums2)}

    def add(self, index: int, val: int) -> None:
        if index not in self.m2_index:
            raise Exception("None existent index")

        old_val = self.m2_index[index]
        self.m2[old_val] -= 1

        self.m2_index[index] += val

        new_val = self.m2_index[index]
        self.m2[new_val] += 1

        return None

    def count(self, tot: int) -> int:
        count = 0
        for v, c in self.m1.items():
            complement = tot - v
            count += c * self.m2[complement]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
