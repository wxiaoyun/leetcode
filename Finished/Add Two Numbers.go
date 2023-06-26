package leetcode

import "leetcode/ds"

func addTwoNumbers(l1 *ds.ListNode, l2 *ds.ListNode) *ds.ListNode {
	return helper5(l1, l2, 0)
}

func helper5(l1 *ds.ListNode, l2 *ds.ListNode, carry int) *ds.ListNode {
	if l1 == nil && l2 == nil && carry == 0 {
		return nil
	}

	if l1 == nil && l2 == nil && carry == 1 {
		return &ds.ListNode{Val: 1, Next: nil}
	}

	if l1 == nil {
		nextVal := carry + l2.Val

		if nextVal >= 10 {
			return &ds.ListNode{Val: nextVal % 10, Next: helper5(nil, l2.Next, 1)}
		}

		return &ds.ListNode{Val: nextVal, Next: helper5(nil, l2.Next, 0)}

	} else if l2 == nil {
		nextVal := carry + l1.Val

		if nextVal >= 10 {
			return &ds.ListNode{Val: nextVal % 10, Next: helper5(l1.Next, nil, 1)}
		}

		return &ds.ListNode{Val: nextVal, Next: helper5(l1.Next, nil, 0)}

	} else {
		nextVal := carry + l1.Val + l2.Val

		if nextVal >= 10 {
			return &ds.ListNode{Val: nextVal % 10, Next: helper5(l1.Next, l2.Next, 1)}
		}

		return &ds.ListNode{Val: nextVal, Next: helper5(l1.Next, l2.Next, 0)}
	}
}
