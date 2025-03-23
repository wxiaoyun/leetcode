from collections import defaultdict

# https://leetcode.com/problems/number-of-wonderful-substrings


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        # The count of a letter is either even or odd
        # a wonderful string can only have 0 or 1 letter that has odd count
        # when we choose to include a letter:
        # - we make previously odd count letter now even

        count = defaultdict(int)
        count[0] = 1

        a_ord = ord("a")
        cur_mask = 0
        total = 0
        for ch in word:
            bit = ord(ch) - a_ord

            cur_mask ^= 1 << bit

            # Case 1: all characters even count:
            # We need an identical mask so that count of all characters are even
            target = cur_mask
            if target in count:
                total += count[target]
            count[cur_mask] += 1

            # Case 2: 1 character odd count:
            for odd_bit in range(10):
                # we need a mask that is (a ^ a ^ odd_bit_mask) = odd_bit_mask
                target = cur_mask ^ (1 << odd_bit)
                if target in count:
                    total += count[target]

        return total
