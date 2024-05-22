# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = deque()
        dq.append((0, root))
        output = []

        while len(dq) > 0:
            (l, n) = dq.popleft()

            if n == None:
                continue
            
            while len(output) <= l:
                output.append([])

            dq.append((l+1, n.left))
            dq.append((l+1, n.right))
            output[l].append(n.val)
        
        return [row[-1] for row in output]
        
