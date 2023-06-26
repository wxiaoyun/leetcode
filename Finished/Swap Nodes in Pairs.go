package leetcode

import "leetcode/ds"

func swapPairs(head *ds.ListNode) *ds.ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	currHead := head
	next := head.Next
	nextNext := swapPairs(head.Next.Next)

	next.Next = head
	currHead.Next = nextNext
	return next
}
