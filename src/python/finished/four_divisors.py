import math
from collections import defaultdict
from typing import Dict, List


# O(n^3/2)
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        cache = {}

        def prime_factors(n: int) -> Dict[int, int]:
            if n in cache:
                return cache[n]
            # print("pfac", n)
            factors = defaultdict(int)
            for d in range(2, math.floor(math.sqrt(n)) + 1):
                if n % d != 0:
                    continue

                for fac, m in prime_factors(d).items():
                    factors[fac] += m
                for fac, m in prime_factors(n // d).items():
                    factors[fac] += m
                break

            if len(factors) == 0:
                factors[n] = 1
            cache[n] = factors
            return factors

        total = 0
        factors = {}
        for n in nums:
            if n in factors:
                if len(factors[n]) == 4:
                    total += sum(factors[n])
                continue

            prime_fac = prime_factors(n)

            two_prime = len(prime_fac) == 2 and sum(prime_fac.values()) == 2
            one_prime_cude = len(prime_fac) == 1 and sum(prime_fac.values()) == 3
            if not (two_prime or one_prime_cude):
                factors[n] = []
                continue

            factor = set([1])
            for fac, m in prime_fac.items():
                for _ in range(m):
                    prev_fac = list(factor)
                    for pfac in prev_fac:
                        factor.add(pfac * fac)
            factors[n] = factor
            total += sum(factor)

        return total


# O(n^2) TLE
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        cache = {}
        def divisor_of(n: int) -> List[int]:
            if n in cache:
                return cache[n]

            divisors = [1]
            for d in range(2, math.ceil(n / 2) + 1):
                if n % d == 0:
                    divisors.append(d)
            divisors.append(n)
            cache[n] = divisors
            return divisors

        total = 0
        for n in nums:
            div = divisor_of(n)
            if len(div) != 4:
                continue

            total += sum(div)
        return total
