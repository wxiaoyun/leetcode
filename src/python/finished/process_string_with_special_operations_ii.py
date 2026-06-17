# https://leetcode.com/problems/process-string-with-special-operations-ii/


class Solution:
    def processStr(self, s: str, k: int) -> str:
        # append
        # - len = len + 1
        # - q = q
        # remove
        # - len = len - 1
        # - q = q
        # dup
        # - len = len + len
        # - q = q
        # rev
        # - len = len
        # - q = len - 1 - q

        size = 0
        for cmd in s:
            if cmd == "*":
                size = max(0, size - 1)
            elif cmd == "#":
                size *= 2
            elif cmd == "%":
                pass
            else:
                size += 1

        q = k
        if q >= size:
            return "."

        for i in reversed(range(len(s))):
            cmd = s[i]
            if cmd == "*":
                size += 1
            elif cmd == "#":
                hsize = size // 2
                if hsize > 0:
                    q %= size // 2
                    size //= 2
            elif cmd == "%":
                q = size - 1 - q
            else:
                size = max(0, size - 1)
                if q == size:
                    return s[i]
        return "."
