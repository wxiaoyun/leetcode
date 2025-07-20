from typing import List

# https://leetcode.com/problems/delete-duplicate-folders-in-system


class Trie:
    def __init__(self):
        self.children = {}
        self.deleted = False
        self.serialize_cache = None
        return None

    def delete(self) -> None:
        self.deleted = True
        return None

    def insert(self, path: List[str], index: int = 0) -> None:
        if index >= len(path):
            return None
        p = path[index]
        if p not in self.children:
            self.children[p] = Trie()
        return self.children[p].insert(path, index + 1)

    def serialize(self) -> str:
        if self.serialize_cache is not None:
            return self.serialize_cache

        builder = []
        for p in sorted(self.children.keys()):
            builder.append(f"{p}({self.children[p].serialize()})")
        self.serialize_cache = "".join(builder)
        return self.serialize_cache


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        t = Trie()
        for p in paths:
            t.insert(p)

        def dfs(t: Trie, seen: dict = {}) -> None:
            s = t.serialize()
            if s == "":
                return None

            if s in seen:
                seen[s].delete()
                t.delete()
                return None
            seen[s] = t

            for t_child in t.children.values():
                dfs(t_child, seen)
            return None

        dfs(t)

        def build_result(
            t: Trie, path_builder: List[str], ret: List[List[str]]
        ) -> None:
            if t.deleted:
                return None
            if len(path_builder) > 0:
                ret.append(path_builder[:])

            for p, t_child in t.children.items():
                path_builder.append(p)
                build_result(t_child, path_builder, ret)
                path_builder.pop()
            return None

        ret = []
        build_result(t, [], ret)
        return ret
