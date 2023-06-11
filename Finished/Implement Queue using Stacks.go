package leetcode

// Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

// Implement the MyQueue class:

// void push(int x) Pushes element x to the back of the queue.
// int pop() Removes the element from the front of the queue and returns it.
// int peek() Returns the element at the front of the queue.
// boolean empty() Returns true if the queue is empty, false otherwise.
// Notes:

// You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
// Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

// Example 1:

// Input
// ["MyQueue", "push", "push", "peek", "pop", "empty"]
// [[], [1], [2], [], [], []]
// Output
// [null, null, null, 1, 1, false]

// Explanation
// MyQueue myQueue = new MyQueue();
// myQueue.push(1); // queue is: [1]
// myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
// myQueue.peek(); // return 1
// myQueue.pop(); // return 1, queue is [2]
// myQueue.empty(); // return false

// Constraints:

// 1 <= x <= 9
// At most 100 calls will be made to push, pop, peek, and empty.
// All the calls to pop and peek are valid.

// Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

// https://leetcode.com/problems/implement-queue-using-stacks/

type MyQueue struct {
	ptr1   int
	ptr2   int
	stack1 []int
	stack2 []int
}

func Constructor() MyQueue {
	return MyQueue{
		ptr1:   0,
		ptr2:   0,
		stack1: []int{},
		stack2: []int{},
	}
}

func (this *MyQueue) Push(x int) {
	if this.ptr1 >= len(this.stack1) {
		this.stack1 = append(this.stack1, x)
	} else {
		this.stack1[this.ptr1] = x
	}
	this.ptr1++
}

func (this *MyQueue) Pop() int {
	this.Peek()
	this.ptr2--
	return this.stack2[this.ptr2]
}

func (this *MyQueue) Peek() int {
	if this.ptr2 != 0 {
		return this.stack2[this.ptr2-1]
	}

	for this.ptr1 != 0 {
		this.ptr1--
		if this.ptr2 >= len(this.stack2) {
			this.stack2 = append(this.stack2, this.stack1[this.ptr1])
		} else {
			this.stack2[this.ptr2] = this.stack1[this.ptr1]
		}
		this.ptr2++
	}
	return this.stack2[this.ptr2-1]
}

func (this *MyQueue) Empty() bool {
	return this.ptr1 == 0 && this.ptr2 == 0
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */
