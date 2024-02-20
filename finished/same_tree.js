// https://leetcode.com/problems/same-tree/submissions/
//
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
  // both is null
  if (p === null && q === null) {
    return true;
  }

  // either is null
  if (p === null || q === null) {
    return false;
  }

  // both is not null

  // check that both current node is the same
  if (p.val !== q.val) {
    return false;
  }

  // both left and right subtree needs to be the same
  return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
