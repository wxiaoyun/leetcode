# https://leetcode.com/problems/vowels-game-in-a-string/


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # alice needs to remove at least 1 vowel, or odd number of vowels
        # bob need to remove at least 1 chr and even number of vowels

        # Case 1: suppose there is 2n + 1 vowel -> alice can remove every character -> alice wins
        # Case 2: suppose there is 2n vowel
        #        - 0 vowel -> alice lose
        #       - else alice removes 2n - 1 vowel -> 1 vowel left -> bob cannot remove odd number, alice wins

        vowels = set(list("aeiou"))
        vowel_count = sum(1 if ch in vowels else 0 for ch in s)
        return vowel_count > 0
