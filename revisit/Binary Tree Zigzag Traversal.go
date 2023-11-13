package leetcode

import "leetcode/util"

// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *util.TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	var result [][]int
	queue := []*util.TreeNode{root}
	zigzag := false

	for len(queue) > 0 {
		levelSize := len(queue)
		level := make([]int, levelSize)

		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]

			// Insert the node value at the correct position based on zigzag order.
			if zigzag {
				level[levelSize-1-i] = node.Val
			} else {
				level[i] = node.Val
			}

			// Add children to the queue.
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		result = append(result, level)
		zigzag = !zigzag // Alternate the direction for the next level.
	}

	return result
}
