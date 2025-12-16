from typing import List

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def gen(digits: str, i: int, output: List[List[str]], builder: List[str]):
            if i >= len(digits):
                if builder:
                    output.append("".join(builder))
                return

            d = digits[i]
            for char in num_to_char[d]:
                builder.append(char)
                gen(digits, i + 1, output, builder)
                builder.pop()

        output = []
        gen(digits, 0, output, [])
        return output
