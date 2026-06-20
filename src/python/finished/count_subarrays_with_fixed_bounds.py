from typing import List

# https://leetcode.com/problems/count-subarrays-with-fixed-bounds


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        cnt = 0

        violate_idx = -1

        min_stk = []  # monotonically increasing
        max_stk = []  # monotonically decreasing
        for i, n in enumerate(nums):
            while min_stk and (nums[min_stk[-1]] >= n or nums[min_stk[-1]] < minK):
                min_stk.pop()
            min_stk.append(i)

            while max_stk and (nums[max_stk[-1]] <= n or nums[max_stk[-1]] > maxK):
                max_stk.pop()
            max_stk.append(i)

            done = False
            while not done:
                done = True
                if min_stk and (min_stk[0] < violate_idx or nums[min_stk[0]] < minK):
                    violate_idx = max(violate_idx, min_stk.pop())
                    done = False

                if max_stk and (max_stk[0] < violate_idx or nums[max_stk[0]] > maxK):
                    violate_idx = max(violate_idx, max_stk.pop())
                    done = False

            # print(i)
            # print(list((i, nums[i]) for i in min_stk))
            # print(list((i, nums[i]) for i in max_stk))
            # print(violate_idx)

            if not (min_stk and max_stk) or (
                nums[min_stk[0]] != minK or nums[max_stk[0]] != maxK
            ):
                continue

            l = violate_idx
            r = min(min_stk[0], max_stk[0])
            # print(l, r)
            cnt += max(0, r - l)

        return cnt


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def count_continguous(arr: List[int], k: int) -> List[int]:
            N = len(arr)
            res = []
            i = 0
            while i < N:
                while i < N and arr[i] != k:
                    i += 1

                count = 0
                while i < N and arr[i] == k:
                    count += 1
                    i += 1

                if count > 0:
                    res.append(count)
            return res

        if minK == maxK:
            segs = count_continguous(nums, minK)
            return sum([s * (s + 1) // 2 for s in segs])  # (s + 1) choose 2

        def split_subarray(arr: List[int], mn: int, mx: int) -> List[List[int]]:
            N = len(arr)
            res = []
            i = 0

            while i < N:
                while i < N and (arr[i] < mn or arr[i] > mx):
                    i += 1

                subarr = []
                while i < N and (arr[i] >= mn and arr[i] <= mx):
                    subarr.append(arr[i])
                    i += 1

                if len(subarr) > 0:
                    res.append(subarr)

            return res

        subarrays = split_subarray(nums, minK, maxK)
        # print(subarrays)

        def count(arr: List[int], mn: int, mx: int) -> int:
            N = len(arr)
            mn_i, mx_i = -1, -1
            # print(arr)

            count = 0
            for i, n in enumerate(arr):
                if n == mn:
                    mn_i = i
                elif n == mx:
                    mx_i = i

                count += min(mn_i, mx_i) + 1
                # print(mn_i, mx_i, min(mn_i, mx_i), i)

            return count

        return sum([count(arr, minK, maxK) for arr in subarrays])
