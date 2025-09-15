# https://leetcode.com/problems/maximum-number-of-words-you-can-type/


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        return len(words) - sum(
            1 if any(ch in brokenLetters for ch in w) else 0 for w in words
        )


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        word_masks = [0] * len(words)

        for i, w in enumerate(words):
            mask = 0
            for ch in w:
                mask |= 1 << (ord(ch) - ord("a"))
            word_masks[i] = mask

        bad_mask = 0
        for ch in brokenLetters:
            bad_mask |= 1 << (ord(ch) - ord("a"))

        return sum(0 if (bad_mask & word_mask) else 1 for word_mask in word_masks)
