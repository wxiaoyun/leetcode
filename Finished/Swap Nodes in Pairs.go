package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
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
