# https://leetcode.com/problems/create-binary-tree-from-descriptions


from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        LEFT = 1
        node_in_degree = {}
        out_edges = defaultdict(list)
        desc_lookup = {}
        build_set = set()

        for p, c, l in descriptions:
            node_in_degree.setdefault(p, 0)
            node_in_degree.setdefault(c, 0)
            node_in_degree[c] += 1
            desc_lookup[c] = (p, l)

            build_set.discard(c)
            if node_in_degree[p] == 0:
                build_set.add(p)

            out_edges[p].append(c)

        assert len(build_set) == 1
        root_val = build_set.pop()
        DUMMY_VAL = -1
        DUMMY_ROOT = TreeNode(DUMMY_VAL)
        desc_lookup[root_val] = (DUMMY_VAL, LEFT)
        node_lookup = {DUMMY_VAL: DUMMY_ROOT}
        build_set.add(root_val)

        while build_set:
            node_val = build_set.pop()
            node = node_lookup.setdefault(node_val, TreeNode(val=node_val))
            node_par, node_dir = desc_lookup[node_val]
            assert node_par in node_lookup

            if node_dir == LEFT:
                node_lookup[node_par].left = node
            else:
                node_lookup[node_par].right = node

            for child in out_edges[node_val]:
                node_in_degree[child] -= 1
                if node_in_degree[child] == 0:
                    build_set.add(child)

        return DUMMY_ROOT.left


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}  # Dict[int, TreeNode]
        parent = {}  # Dict[int, int]

        for p, c, left in descriptions:
            if p not in nodes:
                pnode = TreeNode(p)
                nodes[p] = pnode
            else:
                pnode = nodes[p]

            if c not in nodes:
                cnode = TreeNode(c)
                nodes[c] = cnode
            else:
                cnode = nodes[c]

            if left == 1:
                pnode.left = cnode
            else:
                pnode.right = cnode

            parent[c] = p

        cur = descriptions[0][0]
        while cur in parent:
            cur = parent[cur]

        return nodes[cur]
