# https://leetcode.com/problems/valid-word

import re


class Solution:
    def isValid(self, word: str) -> bool:
        return (
            re.match(
                r"^(?=.*[aeiouAEIOU])(?=.*(?![aeiouAEIOU])[a-zA-Z])[0-9a-zA-Z]{3,}$",
                word,
            )
            is not None
        )
