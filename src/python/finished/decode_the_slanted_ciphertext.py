# https://leetcode.com/problems/decode-the-slanted-ciphertext


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        ncol = len(encodedText) // rows

        ans = ["*"] * (rows * ncol)

        for i in range(rows):
            for j in range(ncol):
                if i * ncol + i + j >= len(encodedText):
                    break
                ans[j * rows + i] = encodedText[i * ncol + i + j]

        j = len(ans) - 1
        while j >= 0 and ans[j] in "* ":
            j -= 1

        return "".join(ans[: j + 1])
