from collections import deque
from typing import List


# https://leetcode.com/problems/reveal-cards-in-increasing-order/


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ordering = []
        rem = deque(range(n))
        while rem:
            idx_in_new_deck = rem.popleft()
            sorted_idx = len(ordering)
            ordering.append((idx_in_new_deck, sorted_idx))

            if rem:
                top = rem.popleft()
                rem.append(top)

        deck_sorted = sorted(deck)
        new_deck = [0] * n
        for idx_in_new_deck, sorted_idx in ordering:
            new_deck[idx_in_new_deck] = deck_sorted[sorted_idx]
        return new_deck
