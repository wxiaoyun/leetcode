package todos

import "leetcode/ds"

// https://leetcode.com/problems/binary-tree-level-order-traversal/

func levelOrder(root *ds.TreeNode) [][]int {
	return levelOrderHelper(root, 0, [][]int{})
}

func levelOrderHelper(node *ds.TreeNode, depth int, output [][]int) [][]int {
	if node == nil {
		return output
	}

	if len(output) >= depth+1 {
		output = append(output, []int{})
	}

	output[depth] = append(output[depth], node.Val)
	output = levelOrderHelper(node.Left, depth+1, output)
	return levelOrderHelper(node.Right, depth+1, output)
}

// func levelOrder(root *ds.TreeNode) [][]int {
// 	if root == nil {
// 		return [][]int{}
// 	}

// 	left := levelOrder(root.Left)
// 	right := levelOrder(root.Right)

// 	result := [][]int{[]int{root.Val}}
// 	for i := 0; i < maxInt(len(left), len(right)); i++ {
// 		if i >= len(left) {
// 			result = append(result, right[i])
// 		} else if i >= len(right) {
// 			result = append(result, left[i])
// 		} else {
// 			result = append(result, append(left[i], right[i]...))
// 		}
// 	}

// 	return result
// }

// func maxInt(a, b int) int {
// 	if a > b {
// 		return a
// 	}
// 	return b
// }
