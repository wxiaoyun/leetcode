// https://leetcode.com/problems/path-sum/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
  return helper(root, 0, targetSum);
};

function helper(node, carry, targetSum) {
  if (node === null) return false; // Return false if node is null

  carry += node.val; // Update carry

  // Check if leaf node
  if (node.left === null && node.right === null) {
    return carry === targetSum;
  }

  return (
    helper(node.left, carry, targetSum) || helper(node.right, carry, targetSum)
  );
}
