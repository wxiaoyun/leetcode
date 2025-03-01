package leetcode

// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	cur := head

	for cur != nil && cur.Next != nil {
		nextNext := cur.Next
		cur.Next = &ListNode{Val: GCD(cur.Val, nextNext.Val)}
		cur.Next.Next = nextNext
		cur = nextNext
	}

	return head
}

func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// func GCD(a, b int) int {
//   c := 0
//   if a > b {
//     c = b
//   } else {
//     c = a
//   }

//   for i := c; i >= 1; i-- {
//     if a % i == 0 && b % i == 0 {
//       return i
//     }
//   }
//   return -1
// }
