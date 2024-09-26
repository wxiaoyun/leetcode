package leetcode

// https://leetcode.com/problems/split-linked-list-in-parts/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func splitListToParts(head *ListNode, k int) []*ListNode {
	length := 0
	cur := head
	for cur != nil {
		length++
		cur = cur.Next
	}

	minLen := length / k
	rmd := length % k

	dummyHeads := make([]*ListNode, k)
	curNode := make([]*ListNode, k)
	for i := 0; i < k; i++ {
		ln := &ListNode{}
		dummyHeads[i] = ln
		curNode[i] = ln
	}

	cur = head
	for i := 0; i < k; i++ {
		ln := minLen
		if rmd > 0 {
			ln++
		}
		rmd--

		for j := 0; j < ln; j++ {
			next := cur.Next
			curNode[i].Next = cur
			curNode[i] = cur
			cur.Next = nil
			cur = next
		}
	}

	for i, dh := range dummyHeads {
		dummyHeads[i] = dh.Next
	}
	return dummyHeads
}
