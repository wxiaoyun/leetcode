package leetcode

// https://leetcode.com/problems/linked-list-in-binary-tree

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubPath(head *ListNode, root *TreeNode) bool {
	if head == nil {
		return true
	}

	// head is not nil
	if root == nil {
		return false
	}
	// head and root is not nil
	if head.Val == root.Val {
		if isContSubPath(head.Next, root.Left) || isContSubPath(head.Next, root.Right) {
			return true
		}
	}

	return isSubPath(head, root.Left) || isSubPath(head, root.Right)
}

func isContSubPath(head *ListNode, root *TreeNode) bool {
	if head == nil {
		return true
	}

	// head is not nil
	if root == nil {
		return false
	}

	// head and root is not nil
	if head.Val == root.Val {
		return isContSubPath(head.Next, root.Left) || isContSubPath(head.Next, root.Right)
	}

	return false
}
