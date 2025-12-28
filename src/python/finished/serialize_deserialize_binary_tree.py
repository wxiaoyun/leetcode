# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        builder = []

        def helper(node):
            if node is None:
                builder.append("X")
                return

            builder.append("(")
            helper(node.left)
            builder.append(str(node.val))
            helper(node.right)
            builder.append(")")
            return

        helper(root)
        return "".join(builder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        cursor = 0

        def helper(data: str):
            nonlocal cursor
            assert cursor < len(data)

            match data[cursor]:
                case s if s == "X":
                    cursor += 1
                    return None
                case s if s == "(":
                    cursor += 1

                    ltree = helper(data)

                    i = cursor
                    if data[cursor] == "-":
                        cursor += 1
                    while data[cursor].isdigit():
                        cursor += 1
                    val = int(data[i:cursor])

                    rtree = helper(data)

                    tn = TreeNode(val)
                    tn.left = ltree
                    tn.right = rtree

                    assert data[cursor] == ")"
                    cursor += 1

                    return tn
                case _:
                    assert False

        return helper(data)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
