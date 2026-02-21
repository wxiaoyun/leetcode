import math

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        n = 21
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False

        for i in range(math.ceil(math.sqrt(n))):
            if not is_prime[i]:
                continue

            for j in range(i**2, n, i):
                is_prime[j] = False

        def n_set(n: int) -> int:
            bits = 0
            while n != 0:
                bits += n & 1
                n >>= 1
            return bits

        return sum(1 if is_prime[n_set(n)] else 0 for n in range(left, right + 1))
