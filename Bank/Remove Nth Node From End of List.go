package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if n == 0 {
		return head
	}

	length := helper(head, n)
	if length == n {
		return head.Next
	}

	return head
}

func helper(l *ListNode, n int) int {
	if l == nil {
		return 0
	}

	length := 1 + helper(l.Next, n)
	if length == n+1 {
		l.Next = l.Next.Next
	}
	return length
}
