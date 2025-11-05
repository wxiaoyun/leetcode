from sortedcontainers import SortedList
from collections import deque, defaultdict
from typing import List

# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)

        q = deque()
        cnt = defaultdict(int)
        freq = SortedList(key=lambda num: (-cnt[num], -num))
        top_x = 0

        def mutate(num: int, delta: int) -> None:
            is_prev_top_x = False
            if num in freq:
                num_idx = freq.index(num)
                if num_idx < x:
                    is_prev_top_x = True
                freq.discard(num)

            prev_cnt = cnt[num]
            now_cnt = prev_cnt + delta
            cnt[num] = now_cnt

            freq.add(num)
            num_idx = freq.index(num)
            is_now_top_x = num_idx < x

            if is_prev_top_x == is_now_top_x:
                if is_prev_top_x:
                    nonlocal top_x
                    top_x += num * delta
                return None

            if is_prev_top_x and not is_now_top_x:
                top_x -= num * prev_cnt

                new_el = freq[x - 1]
                top_x += new_el * cnt[new_el]

                return None

            # not prev_top x and now top x
            top_x += num * now_cnt
            if len(freq) >= x + 1:
                old_el = freq[x]
                top_x -= old_el * cnt[old_el]

            return None

        for i in range(n):
            if len(q) == k:
                pnum = q.popleft()
                mutate(pnum, -1)

            num = nums[i]
            q.append(num)
            mutate(num, 1)

            if len(q) == k:
                ans[i - k + 1] = top_x

        return ans
