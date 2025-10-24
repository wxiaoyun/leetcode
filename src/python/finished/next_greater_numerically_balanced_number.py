from typing import List
import bisect

# https://leetcode.com/problems/next-greater-numerically-balanced-number/


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        digits = len(str(n))
        max_digits = digits + 1

        def permutate(candidates: set, freq: dict, builder: int):
            keys = list(freq.keys())
            if not keys and builder > 0:
                candidates.add(builder)

            for k in keys:
                freq[k] -= 1
                if freq[k] == 0:
                    del freq[k]
                permutate(candidates, freq, builder * 10 + k)
                freq[k] = freq.get(k, 0) + 1

            return None

        def gen_candidates(
            candidates: set, total_digits: int, cur_digit: int, nums: List[int]
        ) -> None:
            if total_digits > max_digits:
                return None

            if cur_digit > 9:
                freq = {n: n for n in nums}
                permutate(candidates, freq, 0)
                return None

            # skip
            gen_candidates(candidates, total_digits, cur_digit + 1, nums)
            # use cur_digit
            nums.append(cur_digit)
            gen_candidates(candidates, total_digits + cur_digit, cur_digit + 1, nums)
            nums.pop()
            return None

        candidates = set()
        gen_candidates(candidates, 0, 1, [])
        bal_nums = list(candidates)
        bal_nums.sort()
        return bal_nums[bisect.bisect_left(bal_nums, n + 1)]
