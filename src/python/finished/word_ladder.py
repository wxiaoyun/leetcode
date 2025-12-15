from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/word-ladder/


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        word_set.add(beginWord)
        word_set.add(endWord)
        wlen = len(beginWord)
        index_chars = [set() for _ in range(wlen)]
        for w in word_set:
            for i, c in enumerate(w):
                index_chars[i].add(c)

        adj_list = defaultdict(list)
        for w in word_set:
            wlist = list(w)
            for i in range(wlen):
                org_ch = w[i]

                for alt_ch in index_chars[i]:
                    if org_ch == alt_ch:
                        continue

                    wlist[i] = alt_ch
                    w_other = "".join(wlist)
                    if w_other not in word_set:
                        continue

                    adj_list[w].append(w_other)

                wlist[i] = org_ch

        q = deque([(beginWord, 1)])
        visited = set()
        while q:
            w, s = q.popleft()
            if w in visited:
                continue
            visited.add(w)

            if w == endWord:
                return s

            for nb in adj_list[w]:
                q.append((nb, s + 1))

        return 0
