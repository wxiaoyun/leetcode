# Lowest Common Ancestor of a Binary Search Tree
# Medium
# 9.4K
# 266
# Companies
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
# Accepted
# 1.2M
# Submissions
# 1.9M
# Acceptance Rate
# 61.9%

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currLowest = root
        isCommonAncestor = True

        while (isCommonAncestor):
            isCommonAncestor = False

            # this case should be impossible to reach
            if (currLowest is None):
                continue
            
            if (self.isCommonAncestor(currLowest.left, p, q)):
                currLowest = currLowest.left
                isCommonAncestor = True 
            
            elif (self.isCommonAncestor(currLowest.right, p , q)):
                currLowest = currLowest.right
                isCommonAncestor = True 
        
        return currLowest
    
    def isCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        return self.findNode(root, p) and self.findNode(root, q)
    
    def findNode(self, root: TreeNode, p: TreeNode) -> bool:
        if (root is None):
            return False
        elif (p.val == root.val):
            return True
        elif (p.val < root.val):
            return self.findNode(root.left, p)
        else:
            return self.findNode(root.right, p)