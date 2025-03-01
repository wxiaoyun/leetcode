package leetcode

// https://leetcode.com/problems/design-circular-deque/

type MyCircularDeque struct {
	maxLen int
	data   []int
	i      int // Idx of first item
	j      int // Idx AFTER the last item
}

func MCDConstructor(k int) MyCircularDeque {
	return MyCircularDeque{
		maxLen: k,
		data:   make([]int, k),
		i:      0,
		j:      0,
	}
}

func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}

	this.i--
	this.data[(this.i+this.maxLen)%this.maxLen] = value
	return true
}

func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}

	this.data[(this.j+this.maxLen)%this.maxLen] = value
	this.j++
	return true
}

func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}

	this.i++
	return true
}

func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}

	this.j--
	return true
}

func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}

	return this.data[(this.i+this.maxLen)%this.maxLen]
}

func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}

	return this.data[(this.j-1+this.maxLen)%this.maxLen]
}

func (this *MyCircularDeque) Len() int {
	return this.j - this.i
}

func (this *MyCircularDeque) IsEmpty() bool {
	return this.Len() == 0
}

func (this *MyCircularDeque) IsFull() bool {
	return this.Len() == this.maxLen
}

/**
* Your MyCircularDeque object will be instantiated and called as such:
* obj := Constructor(k);
* param_1 := obj.InsertFront(value);
* param_2 := obj.InsertLast(value);
* param_3 := obj.DeleteFront();
* param_4 := obj.DeleteLast();
* param_5 := obj.GetFront();
* param_6 := obj.GetRear();
* param_7 := obj.IsEmpty();
* param_8 := obj.IsFull();
 */
