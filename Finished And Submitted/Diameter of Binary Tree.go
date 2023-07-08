package leetcode

import "math"

// Given the root of a binary tree, return the length of the diameter of the tree.

// The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

// The length of a path between two nodes is represented by the number of edges between them.

// Example 1:

// Input: root = [1,2,3,4,5]
// Output: 3
// Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
// Example 2:

// Input: root = [1,2]
// Output: 1

// Constraints:

// The number of nodes in the tree is in the range [1, 104].
// -100 <= Node.val <= 100

// https://leetcode.com/problems/diameter-of-binary-tree/

/**
 * Definition for a binary tree node.
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	diameter, _ := helper(root)
	return diameter - 2
}

func helper(node *TreeNode) (diameter int, height int) {
	if node == nil {
		return 0, 0
	}

	leftD, leftHeight := helper(node.Left)
	rightD, rightHeight := helper(node.Right)
	currD := leftHeight + rightHeight + 2

	if leftD > diameter {
		diameter = leftD
	}

	if rightD > diameter {
		diameter = rightD
	}

	if currD > diameter {
		diameter = currD
	}

	if leftHeight > height {
		height = leftHeight
	}

	if rightHeight > height {
		height = rightHeight
	}

	return diameter, height + 1
}