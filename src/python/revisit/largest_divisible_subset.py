from typing import List

# https://leetcode.com/problems/largest-divisible-subset


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        N = len(nums)
        dp = [1] * N
        parent = [i for i in range(N)]

        for i in range(N):
            ni = nums[i]
            for j in range(i):
                nj = nums[j]

                if (ni % nj == 0) and (dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1
                    parent[i] = j

        max_subset = -1
        i = -0
        for ii, s in enumerate(dp):
            if s > max_subset:
                max_subset = s
                i = ii

        subset = []
        while True:
            subset.append(nums[i])
            if parent[i] == i:
                break
            i = parent[i]

        subset.reverse()
        return subset


# Memory limit exceeded
# class Solution:
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         # Find a subset of nums such that every pair has a number that is a factor of another

#         t = Trie(-1)
#         for n in nums:
#             t.add(n)

#         subset_rev = t.largest()
#         subset_rev.pop()
#         subset_rev.reverse()
#         return subset_rev

# class Trie:
#     def __init__(self, val: int):
#         self.val = val
#         self.children = {}

#     def add(self, val: int) -> bool:
#         if self.val == val:
#             return False

#         if not (
#             (self.val % val == 0) or
#             (val % self.val == 0)
#         ):
#             return False

#         inserted = False
#         for node in self.children.values():
#             inserted = node.add(val) or inserted

#         if not inserted:
#             self.children[val] = Trie(val)

#         return inserted


#     def largest(self) -> List[int]:
#         best = []
#         for child in self.children.values():
#             child_subset = child.largest()
#             if len(child_subset) > len(best):
#                 best = child_subset
#         best.append(self.val)
#         return best
