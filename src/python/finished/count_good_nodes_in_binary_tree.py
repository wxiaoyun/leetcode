# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # count = 1
        # highest = {}
        # highest[root] = root.val

        # dq = deque()
        # dq.append(root)

        # while len(dq) > 0:
        #     n = dq.popleft()

        #     if n == None:
        #         continue

        #     for c in [n.left, n.right]:
        #         if c == None:
        #             continue
        #         if c.val >= highest[n]:
        #             count += 1
        #         dq.append(c)
        #         highest[c] = max(highest[n], c.val)
        
        # return count

        def dfs(n: TreeNode, highest: int) -> int:
            if n == None:
                return 0
            
            g = 0

            if n.val >= highest:
                g+=1

            highest_new=max(highest,n.val)            
            return g+dfs(n.left,highest_new)+dfs(n.right,highest_new)

        return dfs(root, root.val)
        
