from typing import List

# https://leetcode.com/problems/count-good-triplets


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        count = 0
        mx = max(arr)
        prefix_freq = [0] * (
            mx + 2
        )  # the prefix[n] = the number of elements strictly less than n

        for j in range(N):
            jval = arr[j]
            for k in range(j + 1, N):
                kval = arr[k]
                if abs(jval - kval) > b:
                    continue

                al, ar = jval - a, jval + a
                cl, cr = kval - c, kval + c
                l, r = max(0, al, cl), min(mx, ar, cr)
                count += max(0, prefix_freq[r + 1] - prefix_freq[l])

            for i in range(jval + 1, mx + 2):
                prefix_freq[i] += 1

        return count


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        N = len(arr)
        count = 0

        for i in range(N):
            ii = arr[i]

            for j in range(i + 1, N):
                jj = arr[j]

                if abs(ii - jj) > a:
                    continue

                for k in range(j + 1, N):
                    kk = arr[k]

                    if abs(jj - kk) > b:
                        continue

                    if abs(ii - kk) <= c:
                        count += 1

        return count
