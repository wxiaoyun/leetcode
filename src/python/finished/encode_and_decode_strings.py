from typing import List

# https://neetcode.io/problems/string-encode-and-decode/question


class Solution:
    def __init__(self):
        self.escape = "\\"
        self.delim = "|"
        self.special_chars = f"{self.escape}{self.delim}"

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            for ch in s:
                if ch and ch in self.special_chars:
                    out.append(self.escape)
                out.append(ch)
            out.append(self.delim)
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        out = []
        substr = []
        is_escape = False
        for ch in s:
            if not is_escape and ch == self.escape:
                is_escape = True
            elif is_escape:
                assert ch in self.special_chars
                substr.append(ch)
                is_escape = False
                continue
            elif ch == self.delim:
                out.append("".join(substr))
                substr.clear()
            else:
                substr.append(ch)
        return out
