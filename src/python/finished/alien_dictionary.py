from collections import defaultdict
from typing import List, Optional, Tuple

# https://neetcode.io/problems/foreign-dictionary


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        all_chars = set()
        for w in words:
            for c in w:
                all_chars.add(c)

        def find_rule(ls: str, i: int, gt: str, j: int) -> Optional[Tuple[str, str]]:
            if i == len(ls) or j == len(gt):
                if i < len(ls):
                    return "INVALID"
                return None

            ls_first, gt_first = ls[i], gt[j]
            if ls_first == gt_first:
                return find_rule(ls, i + 1, gt, j + 1)

            return (ls_first, gt_first)

        # if a < b, then there is an edge going from a to b
        adj_list = defaultdict(list)
        in_degree = {}
        for i in range(1, len(words)):
            ls, gt = words[i - 1], words[i]

            rule = find_rule(ls, 0, gt, 0)
            if rule is None:
                continue
            if rule == "INVALID":
                return ""

            a, b = rule
            in_degree[b] = in_degree.setdefault(b, 0) + 1
            in_degree.setdefault(a, 0)
            adj_list[a].append(b)

        leaf_nodes = []
        for a, cnt in in_degree.items():
            if cnt == 0:
                leaf_nodes.append(a)

        rule = []
        while leaf_nodes:
            ch = leaf_nodes.pop()
            rule.append(ch)
            all_chars.remove(ch)

            for nb in adj_list[ch]:
                in_degree[nb] -= 1
                if in_degree[nb] == 0:
                    leaf_nodes.append(nb)

        for ch, cnt in in_degree.items():
            if cnt > 0:
                return ""

        for ch in all_chars:
            rule.append(ch)

        return "".join(rule)
