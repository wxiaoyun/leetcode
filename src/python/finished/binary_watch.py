from typing import List, Tuple

# https://leetcode.com/problems/binary-watch


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def build_time(t: List[int]) -> Tuple[bool, str]:
            assert len(t) == 10

            h = 0
            for i in range(4):
                h = (h << 1) | (t[i] & 1)

            m = 0
            for i in range(4, 10):
                m = (m << 1) | (t[i] & 1)

            if h >= 12 or m >= 60:
                return False, ""

            return True, f"{h}:{m:0>2}"

        def dfs(i: int, rem: int, builder: List[int], out: List[str]) -> None:
            if i >= 10:
                if rem != 0:
                    return
                ok, s = build_time(builder)
                if ok:
                    out.append(s)
                return

            # skip
            builder.append(0)
            dfs(i + 1, rem, builder, out)
            builder.pop()

            # use
            if rem > 0:
                builder.append(1)
                dfs(i + 1, rem - 1, builder, out)
                builder.pop()

            return None

        out = []
        dfs(0, turnedOn, [], out)
        return out
