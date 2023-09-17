// https://leetcode.com/problems/symmetric-tree/

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
 * @return {boolean}
 */
var isSymmetric = function (root) {
  if (root === null) {
    return true;
  }

  root.right = Mirror(root.right);

  return isSame(root.left, root.right);
};

function Mirror(root) {
  if (root === null) {
    return root;
  }

  const left = Mirror(root.left);
  const right = Mirror(root.right);
  root.left = right;
  root.right = left;
  return root;
}

function isSame(left, right) {
  if (left === null && right === null) {
    return true;
  }

  if (left === null || right === null) {
    return false;
  }

  if (left.val !== right.val) {
    return false;
  }

  return isSame(left.left, right.left) && isSame(left.right, right.right);
}
