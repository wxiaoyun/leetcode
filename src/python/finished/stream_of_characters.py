from collections import deque
from typing import List

# https://leetcode.com/problems/stream-of-characters/


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, s: str, index: int = 0):
        if index >= len(s):
            self.is_end = True
            return

        ch = s[index]
        ch_index = ord(ch) - ord("a")
        if self.children[ch_index] is None:
            self.children[ch_index] = Trie()
        self.children[ch_index].insert(s, index + 1)

    def check_prefix(self, s: str, index: int = 0) -> bool:
        if self.is_end:
            return True

        if index >= len(s):
            return False

        ch = s[index]
        ch_index = ord(ch) - ord("a")
        if self.children[ch_index] is None:
            return False
        return self.children[ch_index].check_prefix(s, index + 1)


class StreamChecker:

    def __init__(self, words: List[str]):
        trie = Trie()
        for w in words:
            trie.insert(list(reversed(w)))

        self.trie = trie
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        return self.trie.check_prefix(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
