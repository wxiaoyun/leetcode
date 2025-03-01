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

	output := make([][]int, 0)
	queue := []*util.TreeNode{root}
	zigzag := false

	for len(queue) > 0 {
		qlen := len(queue)
		level := make([]int, qlen)

		for i := 0; i < qlen; i++ {
			var next = queue[0]
			queue = queue[1:] // dequeue

			if zigzag {
				level[qlen-1-i] = next.Val
			} else {
				level[i] = next.Val
			}

			if next.Left != nil {
				queue = append(queue, next.Left)
			}

			if next.Right != nil {
				queue = append(queue, next.Right)
			}
		}

		zigzag = !zigzag

		if len(level) > 0 {
			output = append(output, level)
		}
	}

	return output
}
