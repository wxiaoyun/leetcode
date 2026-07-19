# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        cnt = [0] * 26
        offset = ord("a")
        for ch in s:
            cnt[ord(ch) - offset] += 1

        use = [0] * 26
        stk = []
        for ch in s:
            idx = ord(ch) - offset

            if use[idx]:
                cnt[idx] -= 1
                continue

            while stk:
                lidx = ord(stk[-1]) - offset
                if stk[-1] < ch:
                    break
                if cnt[lidx] == 0 and use[lidx] <= 1:
                    # must keep this char
                    break
                # print(f"pop {stk[-1]}, {use}")
                stk.pop()
                use[lidx] -= 1

            stk.append(ch)
            use[idx] += 1
            cnt[idx] -= 1

        return "".join(stk)
