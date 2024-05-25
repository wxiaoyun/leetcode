# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        subtree_sum = {
            None: (0, 0)
        }

        def compute_sum(n: Optional[TreeNode]) -> Tuple[int, int]:
            if not n:
                return (0, 0)
            
            l_sum, l_count = compute_sum(n.left)
            r_sum, r_count = compute_sum(n.right)
            _sum = n.val + l_sum + r_sum
            count = 1 + l_count + r_count
            subtree_sum[n] = (_sum, count)
            return (_sum, count)
        
        compute_sum(root)

        def compute_move(n: Optional[TreeNode]) -> int:
            if not n:
                return 0
            
            v = n.val
            l_sum, l_count = subtree_sum[n.left]
            r_sum, r_count = subtree_sum[n.right]

            l_diff = abs(l_sum-l_count)
            r_diff = abs(r_sum-r_count)

            return (
                n.val-1
                +l_diff
                +r_diff
                +compute_move(n.left)
                +compute_move(n.right)
            )

        return compute_move(root)
