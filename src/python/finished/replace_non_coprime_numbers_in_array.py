# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

from typing import Dict, Tuple, List
import copy
import math


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        prev_nums = []
        for n in nums:
            cur = n
            while prev_nums:
                prev = prev_nums[-1]
                ab_gcd = math.gcd(prev, cur)

                if ab_gcd <= 1:
                    break

                cur = cur // ab_gcd * prev_nums.pop()

            prev_nums.append(cur)

        return prev_nums


# TLE
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        cache = {}

        def get_factors(n: int) -> Dict[int, int]:
            """
            Get prime factors larger than 1, and their corresponding frequency
            """

            if n <= 1:
                return {}

            if n in cache:
                return cache[n]

            factors = {}
            for f in range(2, n):
                if not n % f == 0:
                    continue

                a, b = n // f, f
                a_factors = get_factors(a)
                b_factors = get_factors(b)

                for k, v in a_factors.items():
                    factors[k] = factors.get(k, 0) + v
                for k, v in b_factors.items():
                    factors[k] = factors.get(k, 0) + v
                break

            if len(factors) == 0:
                factors[n] = 1

            cache[n] = factors
            # print(f"get_fac {n}, {factors}")
            return factors

        def is_coprime(a: Dict[int, int], b: Dict[int, int]) -> bool:
            smaller, larger = a, b
            if len(b) < len(a):
                smaller, larger = b, a

            for k in smaller.keys():
                if k in larger:
                    return True

            return False

        def lcm(a: Dict[int, int], b: Dict[int, int]) -> Tuple[int, Dict[int, int]]:
            lcm_factors = copy.deepcopy(a)

            for k, v in b.items():
                lcm_factors[k] = max(v, lcm_factors.get(k, v))

            num = 1
            for k, v in lcm_factors.items():
                num *= k**v

            return num, lcm_factors

        prev_nums = [nums[0]]
        prev_factors = [get_factors(nums[0])]
        i = 1
        for n in nums[1:]:
            cur_num = n
            cur_factor = get_factors(n)

            while prev_factors and is_coprime(prev_factors[-1], cur_factor):
                prev_num = prev_nums.pop()
                prev_factor = prev_factors.pop()

                cur_num, cur_factor = lcm(prev_factor, cur_factor)

            prev_nums.append(cur_num)
            prev_factors.append(cur_factor)

        return prev_nums
