// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function (root) {
  const traversal = [];
  helper(root, traversal);

  for (let i = 0; i < traversal.length; i++) {
    traversal[i].left = null;
    traversal[i].right = traversal[i + 1] ?? null;
  }
};

function helper(node, array) {
  if (node === null) return;

  array.push(node);
  helper(node.left, array);
  helper(node.right, array);
}
