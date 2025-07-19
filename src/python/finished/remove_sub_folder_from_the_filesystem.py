from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def new_node(end: bool = False):
            return {
                "children": {},
                "end": end,
            }

        root = new_node()
        for f in folder:
            segments = f.split("/")
            cur = root
            for s in segments:
                nd = cur["children"].get(s, new_node())
                cur["children"][s] = nd
                cur = nd
                if nd["end"]:
                    break

            cur["end"] = True

        def dfs(node: dict, builder: List[str], ret: List[str]) -> None:
            if node["end"]:
                ret.append("/".join(builder))
                return

            for seg, c in node["children"].items():
                builder.append(seg)
                dfs(c, builder, ret)
                builder.pop()
            return None

        ret = []
        dfs(root, [], ret)
        return ret
