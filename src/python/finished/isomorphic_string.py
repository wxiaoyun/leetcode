# https://leetcode.com/problems/isomorphic-strings


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()

        for i in range(len(s)):
            fr, to = s[i], t[i]
            if fr in mapping:
                if mapping[fr] != to:
                    return False
                else:
                    continue
            if to in mapped:
                return False
            mapping[fr] = to
            mapped.add(to)

        return True
