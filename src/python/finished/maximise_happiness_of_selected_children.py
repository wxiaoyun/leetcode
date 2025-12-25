import heapq
from typing import List

# https://leetcode.com/problems/maximize-happiness-of-selected-children


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()

        total = 0
        for i in range(k):
            total += max(0, happiness[-1 - i] - i)
        return total


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        k_happy = []  # min heap to remove the least happy kids
        for h in happiness:
            heapq.heappush(k_happy, h)
            if len(k_happy) > k:
                heapq.heappop(k_happy)

        res = 0
        i = k
        while k_happy:
            i -= 1
            h = heapq.heappop(k_happy)
            res += max(0, h - i)
        return res


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(key=lambda h: -h)

        i = 0
        total_happiness = 0
        for h in happiness:
            total_happiness += max(0, h - i)
            i += 1
            if i == k:
                break
        return total_happiness


# Wrong solution, the order within top k matters
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        def partition(arr: List[int], l: int, r: int) -> int:
            if l >= r:
                return l

            pivot = arr[l]

            arr[l], arr[r - 1] = arr[r - 1], arr[l]
            insertion_idx = l

            for j in range(l, r):
                if arr[j] < pivot:
                    arr[j], arr[insertion_idx] = arr[insertion_idx], arr[j]
                    insertion_idx += 1

            arr[insertion_idx], arr[r - 1] = arr[r - 1], arr[insertion_idx]
            return insertion_idx

        def quick_select(arr: List[int], l: int, r: int, n: int) -> int:
            m = partition(arr, l, r)
            if m < n:
                return quick_select(arr, m + 1, r, n)
            if m == n:
                return m
            # n < m
            return quick_select(arr, l, m, n)

        m = quick_select(happiness, 0, len(happiness), len(happiness) - k)

        total = 0
        for i in range(k):
            total += max(0, happiness[-1 - i] - i)
        return total
