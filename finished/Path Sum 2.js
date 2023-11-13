// https://leetcode.com/problems/path-sum-ii/

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
 * @return {number[][]}
 */
var pathSum = function (root, targetSum) {
  const paths = [];
  helper(root, targetSum, paths, 0, []);
  return paths;
};

function helper(node, targetSum, paths, carry, current) {
  if (node === null) return;

  carry += node.val;
  current = [...current, node.val];
  if (node.left === null && node.right === null) {
    if (carry === targetSum) paths.push([...current]);
    return;
  }

  helper(node.left, targetSum, paths, carry, current);
  helper(node.right, targetSum, paths, carry, current);
}
