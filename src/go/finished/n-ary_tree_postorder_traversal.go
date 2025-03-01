package leetcode

// https://leetcode.com/problems/n-ary-tree-postorder-traversal

// Definition for a Node.
type Node struct {
	Val      int
	Children []*Node
}

func postorder(root *Node) []int {
	res := []int{}
	var helper func(*Node)
	helper = func(n *Node) {
		if n == nil {
			return
		}

		for _, c := range n.Children {
			helper(c)
		}
		res = append(res, n.Val)
	}

	helper(root)
	return res
}
