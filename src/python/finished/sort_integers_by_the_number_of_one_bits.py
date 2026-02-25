from typing import List

# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def less_than(a: int, b: int) -> bool:
            a_ones = bin(a).count("1")
            b_ones = bin(b).count("1")
            if a_ones != b_ones:
                return a_ones < b_ones
            return a < b

        def partition(arr: List[int], l: int, r: int) -> int:
            if r - l <= 1:
                return l

            pivot = arr[l]
            arr[l], arr[r - 1] = arr[r - 1], arr[l]

            j = l
            for i in range(l, r):
                if less_than(arr[i], pivot):
                    arr[j], arr[i] = arr[i], arr[j]
                    j += 1

            arr[j], arr[r - 1] = arr[r - 1], arr[j]
            return j

        def quicksort(arr: List[int], l: int, r: int) -> None:
            if r - l <= 1:
                return None

            p = partition(arr, l, r)
            quicksort(arr, l, p)
            quicksort(arr, p + 1, r)
            return None

        cp = arr[:]
        quicksort(cp, 0, len(cp))
        return cp


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda n: (bin(n).count("1"), n))
