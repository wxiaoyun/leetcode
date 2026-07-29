from collections import Counter

# https://leetcode.com/problems/smallest-palindromic-rearrangement-i


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = sorted(Counter(s).items())
        # print(cnt)

        odd_pair = -1
        ans = []
        for i, (ch, c) in enumerate(cnt):
            if c % 2 != 0:
                assert odd_pair < 0
                odd_pair = i

            ans.append(ch * (c // 2))

        if odd_pair >= 0:
            ch, _ = cnt[odd_pair]
            ans.append(ch)

        for ch, c in reversed(cnt):
            ans.append(ch * (c // 2))

        return "".join(ans)
