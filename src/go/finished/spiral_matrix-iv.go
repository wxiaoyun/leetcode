package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func spiralMatrix(m int, n int, head *ListNode) [][]int {
	output := make([][]int, m)
	for i := 0; i < m; i++ {
		output[i] = make([]int, n)
	}

	cur := head
	t, b, l, r := 0, m-1, 0, n-1
	i, j := 0, 0

	for t <= b && l <= r {
		if !(t <= b && l <= r) {
			break
		}
		// Fill top row
		for j < r {
			if cur != nil {
				output[i][j] = cur.Val
				cur = cur.Next
			} else {
				output[i][j] = -1
			}
			j++
		}
		t++

		if !(t <= b && l <= r) {
			break
		}
		// Fill right column
		for i < b {
			if cur != nil {
				output[i][j] = cur.Val
				cur = cur.Next
			} else {
				output[i][j] = -1
			}
			i++
		}
		r--

		if !(t <= b && l <= r) {
			break
		}
		// fill bottom row
		for j > l {
			if cur != nil {
				output[i][j] = cur.Val
				cur = cur.Next
			} else {
				output[i][j] = -1
			}
			j--
		}
		b--

		if !(t <= b && l <= r) {
			break
		}
		// fill left column
		for i > t {
			if cur != nil {
				output[i][j] = cur.Val
				cur = cur.Next
			} else {
				output[i][j] = -1
			}
			i--
		}
		l++
	}

	if cur != nil {
		output[i][j] = cur.Val
	} else {
		output[i][j] = -1
	}

	return output
}
