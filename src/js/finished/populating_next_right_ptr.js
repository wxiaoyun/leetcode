// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function (root) {
  const levels = [];
  helper(root, 0, levels);
  return root;
};

function helper(node, level, levels) {
  if (node === null) return;

  if (levels[level] === undefined) levels[level] = null;

  node.next = levels[level];
  levels[level] = node;

  helper(node.right, level + 1, levels);
  helper(node.left, level + 1, levels);
}
