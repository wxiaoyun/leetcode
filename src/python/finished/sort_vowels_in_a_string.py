# https://leetcode.com/problems/sort-vowels-in-a-string/


class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_set = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        vowels = [ch for ch in s if ch in vowel_set]
        vowels.sort()

        ret = []
        i = 0
        for ch in s:
            if ch not in vowel_set:
                ret.append(ch)
                continue

            ret.append(vowels[i])
            i += 1

        return "".join(ret)
