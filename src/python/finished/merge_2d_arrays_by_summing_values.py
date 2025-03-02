from typing import List

# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        reverse_index = {}
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            i1, v1 = nums1[i]
            i2, v2 = nums2[j]

            if i1 < i2:
                if i1 in reverse_index:
                    idx = reverse_index[i1]
                    res[idx][1] += v1
                else:
                    reverse_index[i1] = len(res)
                    res.append([i1, v1])
                i += 1
            else:
                if i2 in reverse_index:
                    idx = reverse_index[i2]
                    res[idx][1] += v2
                else:
                    reverse_index[i2] = len(res)
                    res.append([i2, v2])
                j += 1

        while i < len(nums1):
            i1, v1 = nums1[i]
            if i1 in reverse_index:
                idx = reverse_index[i1]
                res[idx][1] += v1
            else:
                res.append([i1, v1])
            i += 1

        while j < len(nums2):
            i2, v2 = nums2[j]
            if i2 in reverse_index:
                idx = reverse_index[i2]
                res[idx][1] += v2
            else:
                res.append([i2, v2])
            j += 1

        return res
