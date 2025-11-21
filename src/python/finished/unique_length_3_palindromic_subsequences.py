from collections import defaultdict

# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ch_cnt = defaultdict(int)
        ch_set_pending = defaultdict(set)
        ch_set_between = defaultdict(set)

        for ch in s:
            ch_cnt[ch] += 1

            for other_ch, cnt in ch_cnt.items():
                if cnt == 0:
                    continue
                ch_set_pending[other_ch].add(ch)

            if ch_cnt[ch] >= 2:
                pending = ch_set_pending[ch]
                ch_set_between[ch].update(pending)

        total = 0
        for ch, cnt in ch_cnt.items():
            if cnt < 2:
                continue
            between_cnt = len(ch_set_between[ch])
            between_cnt_exclude_ch = between_cnt - 1
            total += between_cnt_exclude_ch

            if cnt >= 3:
                total += 1
        return total


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        freq = defaultdict(int)
        last_seen = {}
        count = set()

        for i, ch in enumerate(s):
            freq[ch] += 1
            if freq[ch] == 3:
                count.add(ch * 3)

            if ch in last_seen:
                last_idx = last_seen[ch]

                for j in range(last_idx + 1, i):
                    count.add(f"{ch}{s[j]}{ch}")

            last_seen[ch] = i

        return len(count)
