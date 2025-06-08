# https://leetcode.com/problems/lexicographical-numbers


class Trie:
    def __init__(self) -> None:
        self.children = [None] * 10
        self.is_end = False

    def insert(self, num: str) -> None:
        def helper(t: Trie, num: str, i: int) -> None:
            if i >= len(num):
                t.is_end = True
                return None

            ch = ord(num[i]) - ord("0")
            if t.children[ch] is None:
                t.children[ch] = Trie()
            return helper(t.children[ch], num, i + 1)

        return helper(self, num, 0)

    def ordered(self) -> List[str]:
        def helper(t: Trie, builder: List[int], result: List[str]):
            if t.is_end:
                num = 0
                for d in builder:
                    num *= 10
                    num += d
                result.append(num)

            for i, child in enumerate(t.children):
                if child is not None:
                    builder.append(i)
                    helper(child, builder, result)
                    builder.pop()
            return None

        builder = []
        res = []
        helper(self, builder, res)
        return res


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        t = Trie()
        for i in range(1, n + 1):
            t.insert(str(i))
        return t.ordered()
