from typing import List

# https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # bin search for pivot, then bin search for target
        l, r = 0, len(nums)
        # invariant: pivot is between l and r
        INF = 1 << 32
        pivot = -1
        while l < r:
            m = l + (r - l) // 2
            # print(l, m, r)

            mleft = nums[m - 1] if m > 0 else -INF
            if mleft > nums[m]:
                # print("m check", m)
                pivot = m
                break

            edge = -1
            if nums[l] < nums[m]:
                # pivot is on our right
                l = m + 1
                edge = l
            else:  # nums[l] > nums[m]
                # we overshot
                r = m
                edge = r

            eleft = nums[edge - 1] if m > 0 else -INF
            if edge < len(nums) and eleft > nums[edge]:
                # print("edge check", edge)
                pivot = edge
                break

        # print("pivot", pivot)

        def bin_search(arr: List[int], l: int, r: int, target: int) -> int:
            # print("check", l, r)
            while l < r:
                m = l + (r - l) // 2
                if arr[m] == target:
                    # print("OK")
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return -1

        rbound = pivot if pivot >= 0 else len(nums)
        if rbound > 0 and nums[0] <= target and target <= nums[rbound - 1]:
            return bin_search(nums, 0, rbound, target)

        lbound = pivot if pivot >= 0 else 0
        if lbound < len(nums) and nums[lbound] <= target and target <= nums[-1]:
            return bin_search(nums, lbound, len(nums), target)

        return -1
