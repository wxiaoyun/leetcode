class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # is there a number i such that (10^i + 10^(i-1) + ... + 10^0) % k = 0
        # (10^i + 10^(i-1) + ... + 10^0) % k = 0 % k
        # (10^i) % k = (0 - (10^i + 10^(i-1) + ... + 10^0) % k) % k
        # We can keep building this sum and check
        #
        # How do we know if such i does not exist?
        #
        # (2):
        # 1 % 2 = 1
        # 11 % 2 = 1
        # 111 % 2 = 1
        #
        # (4):
        # 1 % 4 = 1
        # 11 % 4 = 3
        # 111 % 4 = 3
        # 1111 % 4 = 3
        # 11111 % 4 = 3

        # 1 % 5 = 1
        # 11 % 5 = 1
        # 111 % 5 = 1

        # There seems to be a "cycle" of remainders if such a number does not exist

        # sum_mod_k(i) = (sum_mod_k(i-1) * 10 + 1) % k
        # Each subsequent sum_mod_k is completely determined by the previous
        # sum_mod_k, rather than the actual number, hence, if we observe a
        # repeat, we can conclude that such a number does not exist.

        i = 0
        sum_mod_k = 0
        seen_rem = set()
        while True:
            sum_mod_k = (sum_mod_k * 10 + 1) % k
            if sum_mod_k == 0:
                return i + 1
            if sum_mod_k in seen_rem:
                return -1
            seen_rem.add(sum_mod_k)
            i += 1


