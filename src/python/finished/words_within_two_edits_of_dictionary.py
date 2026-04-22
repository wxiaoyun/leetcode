from typing import List

# https://leetcode.com/problems/words-within-two-edits-of-dictionary


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def editable(src: str, dst: str) -> bool:
            assert len(src) == len(dst)

            diff_cnt = 0
            for i in range(len(src)):
                if src[i] == dst[i]:
                    continue

                diff_cnt += 1
                if diff_cnt > 2:
                    break
            return diff_cnt <= 2

        ans = []
        for q in queries:
            for dst in dictionary:
                if editable(q, dst):
                    ans.append(q)
                    break
        return ans
