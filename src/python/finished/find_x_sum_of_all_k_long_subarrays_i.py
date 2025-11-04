from collections import deque
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        q = deque()
        freq = defaultdict(int)

        for i in range(n):
            if len(q) == k:
                lnum = q.popleft()
                freq[lnum] -= 1
                if freq[lnum] == 0:
                    del freq[lnum]

            num = nums[i]
            q.append(num)
            freq[num] += 1

            if len(q) == k:
                freq_sorted = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
                ans[i - k + 1] = sum(map(lambda p: p[0] * p[1], freq_sorted[:x]))

        return ans
