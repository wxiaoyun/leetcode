# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii

from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        count = sorted(
            [(freq, key) for key, freq in count.items()],
            key=lambda x: -x[0] # most frequently used key to least used key
        )

        i = 0
        cost = 1
        total_cost = 0
        while i < len(count):
            for _ in range(2, 9+1):
                if i >= len(count):
                    break
                freq, _ = count[i]
                total_cost += cost * freq
                i += 1
            cost += 1
        
        return total_cost