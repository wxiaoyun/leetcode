package leetcode

import "leetcode/ds"

// https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

func sumNumbers(root *ds.TreeNode) int {
	results := []int{}
	helper(root, 0, &results)
	result := 0
	for _, num := range results {
		result += num
	}
	return result
}

func helper(node *ds.TreeNode, accum int, results *[]int) {
	if node == nil {
		return
	}

	if isLeaf(node) {
		*results = append(*results, accum*10+node.Val)
	}

	helper(node.Left, accum*10+node.Val, results)
	helper(node.Right, accum*10+node.Val, results)
}

func isLeaf(node *ds.TreeNode) bool {
	if node == nil {
		return false
	}

	return node.Left == nil && node.Right == nil
}

// func sumNumbers(root *ds.TreeNode) int {
// 	var result int
// 	for _, num := range helper(root) {
// 		converted, err := strconv.Atoi(num)
// 		if err != nil {
// 			panic(err)
// 		}
// 		result += converted
// 	}

// 	return result
// }

// // return all the root to leaf path as []string
// func helper(node *ds.TreeNode) []string {
// 	if node == nil {
// 		return []string{}
// 	}

// 	if isLeaf(node) {
// 		return []string{strconv.Itoa(node.Val)}
// 	}

// 	thisChar := strconv.Itoa(node.Val)
// 	leftPaths := helper(node.Left)
// 	rightPaths := helper(node.Right)

// 	output := make([]string, len(leftPaths)+len(rightPaths))
// 	for i, num := range leftPaths {
// 		output[i] = thisChar + num
// 	}
// 	for i, num := range rightPaths {
// 		output[i+len(leftPaths)] = thisChar + num
// 	}

// 	return output
// }
