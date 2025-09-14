from typing import List
import re


# https://leetcode.com/problems/vowel-spellchecker/


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_dict = set(wordlist)
        lower_dict = {}
        vwl_dict = {}

        vwl_reg = re.compile(r"[aeiou]")
        for w in wordlist:
            w_lower = w.lower()
            if w_lower not in lower_dict:
                lower_dict[w_lower] = w

            w_lower_vwl = re.sub(vwl_reg, "*", w_lower)
            if w_lower_vwl not in vwl_dict:
                vwl_dict[w_lower_vwl] = w

        ans = [""] * len(queries)
        for i, q in enumerate(queries):
            if q in exact_dict:
                ans[i] = q
                continue

            q_lower = q.lower()
            if q_lower in lower_dict:
                ans[i] = lower_dict[q_lower]
                continue

            q_lower_vwl = re.sub(vwl_reg, "*", q_lower)
            if q_lower_vwl in vwl_dict:
                ans[i] = vwl_dict[q_lower_vwl]
                continue

        return ans
