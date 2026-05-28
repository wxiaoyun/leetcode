from typing import List

# https://leetcode.com/problems/longest-common-suffix-queries


class Trie:
    def __init__(self):
        self.children = {}
        self.idx = -1

    def insert(self, s: str, idx: int):
        cur = self
        if cur.idx < 0:
            cur.idx = idx

        for ch in s:
            cur = cur.children.setdefault(ch, Trie())
            if cur.idx < 0:
                cur.idx = idx
        return None

    def longest_prefix(self, q: str) -> int:
        cur = self
        ans = cur.idx
        for ch in q:
            if ch not in cur.children:
                return ans
            cur = cur.children[ch]
            ans = cur.idx
        return ans


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        sorted_word_container = [(len(w), i, w) for i, w in enumerate(wordsContainer)]
        sorted_word_container.sort()
        # print(sorted_word_container)

        t = Trie()
        for _l, i, w in sorted_word_container:
            w_rev = "".join(reversed(w))
            # print(f'insert {w_rev}')
            t.insert(w_rev, i)

        n = len(wordsQuery)
        ans = [0] * n
        for i, q in enumerate(wordsQuery):
            q_rev = "".join(reversed(q))
            # print(f"query {q_rev}")
            idx = t.longest_prefix(q_rev)
            ans[i] = idx
        return ans
