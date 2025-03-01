package leetcode

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}

	pivot, leftPreorder, rightPreorder, leftInorder, rightInorder := splitOrders(preorder, inorder)

	return &TreeNode{
		Val:   pivot,
		Left:  buildTree(leftPreorder, leftInorder),
		Right: buildTree(rightPreorder, rightInorder),
	}
}

func splitOrders(preorder, inorder []int) (int, []int, []int, []int, []int) {
	pivot := preorder[0]

	i := 0
	for i < len(inorder) && inorder[i] != pivot {
		i++
	}

	return pivot, preorder[1 : i+1], preorder[i+1:], inorder[:i], inorder[i+1:]
}
