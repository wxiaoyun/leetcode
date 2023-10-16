package leetcode

import "leetcode/util"

func swapPairs(head *util.ListNode) *util.ListNode {
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
