package leetcode

import "leetcode/util"

func removeNthFromEnd(head *util.ListNode, n int) *util.ListNode {
	if n == 0 {
		return head
	}

	length := helper2(head, n)
	if length == n {
		return head.Next
	}

	return head
}

func helper2(l *util.ListNode, n int) int {
	if l == nil {
		return 0
	}

	length := 1 + helper2(l.Next, n)
	if length == n+1 {
		l.Next = l.Next.Next
	}
	return length
}
