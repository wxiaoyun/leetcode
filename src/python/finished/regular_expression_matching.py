# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = []
        plen = len(p)
        i = 0
        while i < plen:
            cur = p[i]
            look_ahead = p[i + 1] if i + 1 < plen else ""

            if look_ahead != "*":
                pattern.append(cur)
                i += 1
                continue

            pattern.append(p[i : i + 2])
            i += 2

        def match(dp: dict, i: int, j: int) -> bool:
            key = (i, j)
            if key in dp:
                return dp[key]

            if i >= len(s) and j >= len(pattern):
                return True

            if i >= len(s) or j >= len(pattern):
                if j < len(pattern) and len(pattern[j]) == 2:
                    return match(dp, i, j + 1)
                return False

            is_match = False
            char_s = s[i]
            patt = pattern[j]

            if len(patt) == 1:
                local_match = char_s == patt or patt == "."
                is_match = is_match or (local_match and match(dp, i + 1, j + 1))

            else:
                assert len(patt) == 2
                assert patt[1] == "*"

                char_pat = patt[0]
                local_match = char_s == char_pat or char_pat == "."

                # we can use the ?* pattern 0 times
                is_match = is_match or match(dp, i, j + 1)

                if local_match:
                    # use the ?* 1 time without consuming
                    is_match = is_match or match(dp, i + 1, j)

                    # use the ?* pattern and consume it
                    is_match = is_match or match(dp, i + 1, j + 1)

            dp[key] = is_match
            return is_match

        return match({}, 0, 0)
