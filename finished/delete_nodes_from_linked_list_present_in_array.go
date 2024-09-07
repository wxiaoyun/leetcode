package leetcode

// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func modifiedList(nums []int, head *ListNode) *ListNode {
	dict := make(map[int]bool)
	for _, n := range nums {
		dict[n] = true
	}

	dummyHead := &ListNode{
		Val:  0,
		Next: head,
	}

	prev, cur := dummyHead, head
	for cur != nil {
		if dict[cur.Val] {
			prev.Next = cur.Next
		} else {
			prev = cur
		}
		cur = cur.Next
	}

	return dummyHead.Next
}

// func modifiedList(nums []int, head *ListNode) *ListNode {
//     dict := make(map[int]bool)
//     for _, n := range nums {
//       dict[n] = true
//     }

//     var helper func(list *ListNode) *ListNode
//     helper = func(list *ListNode) *ListNode {
//       if list == nil {
//         return nil
//       }

//       if dict[list.Val] {
//         return helper(list.Next)
//       }

//       next := helper(list.Next)
//       list.Next = next
//       return list
//     }

//     return helper(head)
// }
