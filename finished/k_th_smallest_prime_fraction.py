from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        result = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                result.append((arr[i]/arr[j], arr[i], arr[j]))

        result.sort(key=lambda v: v[0])

        return (result[k-1][1], result[k-1][2])
