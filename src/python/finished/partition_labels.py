from typing import List

# https://leetcode.com/problems/partition-labels


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        fst = {}
        lst = {}

        for i, ch in enumerate(s):
            if ch not in fst:
                fst[ch] = i
            lst[ch] = i

        intervals = [(fst[ch], lst[ch]) for ch in fst.keys()]
        intervals.sort()

        merged = []
        prev_s, prev_e = intervals[0][0], intervals[0][1]
        for s, e in intervals[1:]:
            if s < prev_e:
                prev_e = max(prev_e, e)
                continue

            merged.append(prev_e - prev_s + 1)
            prev_s, prev_e = s, e

        merged.append(prev_e - prev_s + 1)
        return merged
