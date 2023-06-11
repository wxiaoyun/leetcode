package leetcode

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	return helper(l1, l2, 0)
}

func helper(l1 *ListNode, l2 *ListNode, carry int) *ListNode {
	if l1 == nil && l2 == nil && carry == 0 {
		return nil
	}

	if l1 == nil && l2 == nil && carry == 1 {
		return &ListNode{1, nil}
	}

	if l1 == nil {
		nextVal := carry + l2.Val

		if nextVal >= 10 {
			return &ListNode{nextVal % 10, helper(nil, l2.Next, 1)}
		}

		return &ListNode{nextVal, helper(nil, l2.Next, 0)}

	} else if l2 == nil {
		nextVal := carry + l1.Val

		if nextVal >= 10 {
			return &ListNode{nextVal % 10, helper(l1.Next, nil, 1)}
		}

		return &ListNode{nextVal, helper(l1.Next, nil, 0)}

	} else {
		nextVal := carry + l1.Val + l2.Val

		if nextVal >= 10 {
			return &ListNode{nextVal % 10, helper(l1.Next, l2.Next, 1)}
		}

		return &ListNode{nextVal, helper(l1.Next, l2.Next, 0)}
	}
}
