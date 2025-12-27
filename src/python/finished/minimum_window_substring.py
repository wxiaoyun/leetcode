from collections import Counter

from sortedcontainers import SortedList


# O(m + n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        expected = Counter(t)
        current = {ch: 0 for ch in expected.keys()}
        n_met = 0

        best_l, best_r = 0, len(s)
        l = 0
        for r in range(len(s)):
            r_ch = s[r]
            if r_ch in expected:
                current[r_ch] += 1
                if current[r_ch] == expected[r_ch]:
                    n_met += 1

            while n_met == len(expected):
                if r - l < best_r - best_l:
                    best_l, best_r = l, r

                l_ch = s[l]
                if l_ch in expected:
                    current[l_ch] -= 1

                    if current[l_ch] < expected[l_ch]:
                        n_met -= 1
                l += 1

        return s[best_l : best_r + 1] if best_r < len(s) else ""


# O(mlogn + n)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = Counter(t)

        best_l, best_r = -1, len(s)

        win_cnt = {ch: 0 for ch in t_cnt.keys()}
        # w_cnt[ch] - t_cnt[ch]: < 0 means still need more characters
        # if the lowest number is >= 0, then all the condition is satisfied
        need_queue = SortedList(t_cnt.keys(), key=lambda ch: win_cnt[ch] - t_cnt[ch])
        l = 0
        for r in range(len(s)):
            r_ch = s[r]
            if r_ch in t_cnt:
                need_queue.remove(r_ch)
                win_cnt[r_ch] += 1
                need_queue.add(r_ch)

            while l <= r and win_cnt[need_queue[0]] - t_cnt[need_queue[0]] >= 0:
                if r - l < best_r - best_l:
                    best_l, best_r = l, r

                ch = s[l]
                l += 1
                if ch in t_cnt:
                    need_queue.remove(ch)
                    win_cnt[ch] -= 1
                    need_queue.add(ch)

        return s[best_l : best_r + 1] if best_r - best_l <= len(s) else ""
