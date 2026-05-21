from typing import List

# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix


class Trie:
    def __init__(self):
        self.children = {}

    def insert(self, s: str) -> None:
        cur = self
        for i in range(len(s)):
            ch = s[i]
            cur = cur.children.setdefault(ch, Trie())
        return

    def __str__(self):
        builder = ["("]
        for k, v in self.children.items():
            builder.append(k)
            builder.append(":")
            builder.append(str(v))
        builder.append(")")
        return "".join(builder)


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        t1, t2 = Trie(), Trie()
        for n in arr1:
            # print("1", n)
            t1.insert(str(n))
        for n in arr2:
            # print("2", n)
            t2.insert(str(n))
        # print(t1)
        # print(t2)

        def search(t1: Trie, t2: Trie) -> int:
            keys = set()
            keys.update(t1.children.keys())
            keys.update(t2.children.keys())

            best = 0
            for k in keys:
                if not (k in t1.children and k in t2.children):
                    continue
                best = max(best, 1 + search(t1.children[k], t2.children[k]))
            return best

        return search(t1, t2)
