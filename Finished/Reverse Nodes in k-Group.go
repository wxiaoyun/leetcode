package leetcode

import "leetcode/ds"

func reverseKGroup(head *ds.ListNode, k int) *ds.ListNode {
	// First check if the first k nodes are valid
	cur := head
	for i := 0; i < k; i++ {
		if cur == nil {
			// Not enough to reverse
			return head
		}

		cur = cur.Next
	}

	// at this point, cur is pointing at the k + 1 th node
	// Wishful thinking: Suppose the k+1 th node and onwards are reversed correctly
	// I just need to reverse the first k nodes
	endpoint := reverseKGroup(cur, k)

	prev := endpoint
	cur = head

	for i := 0; i < k; i++ {
		temp := cur.Next
		cur.Next = prev
		prev = cur
		cur = temp
	}
	return prev
}
