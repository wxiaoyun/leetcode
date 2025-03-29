import heapq
from typing import List

# https://leetcode.com/problems/apply-operations-to-maximize-score


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        max_n = max(nums)

        prime_cnt = [0] * (max_n + 1)
        for n in range(2, max_n + 1):
            if prime_cnt[n] > 0:
                continue

            cur = n
            while cur <= max_n:
                prime_cnt[cur] += 1
                cur += n

        next_dom = [N] * N
        prev_dom = [-1] * N
        dec_stack = []
        # stack invariant: bottom - lowest prime count, top - highest prime count

        for r in range(N):
            while dec_stack and prime_cnt[nums[dec_stack[-1]]] < prime_cnt[nums[r]]:
                l = dec_stack.pop()
                next_dom[l] = r

            if dec_stack:
                prev_dom[r] = dec_stack[-1]

            dec_stack.append(r)

        subarr_cnt = [0] * N
        for i in range(N):
            subarr_cnt[i] = (i - prev_dom[i]) * (next_dom[i] - i)

        n2i = [(-n, i) for i, n in enumerate(nums)]
        heapq.heapify(n2i)

        M = (10**9) + 7
        score = 1
        while k > 0:
            n, i = heapq.heappop(n2i)
            n = -n

            cnt = min(k, subarr_cnt[i])
            k -= cnt

            score = (score * pow(n, cnt, M)) % M

        return score
