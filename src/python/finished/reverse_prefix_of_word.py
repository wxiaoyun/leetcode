class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i, c in enumerate(word):
            if c == ch:
                idx = i
                break

        if idx < 0:
            return word

        res = [""] * len(word)
        for i in range(idx + 1):
            res[i] = word[idx - i]
        for i in range(idx + 1, len(word)):
            res[i] = word[i]

        return "".join(res)
