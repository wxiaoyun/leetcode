package leetcode

type CustomStack struct {
	data []int
	max  int
	ptr  int
}

func CCSConstructor(maxSize int) CustomStack {
	return CustomStack{
		data: make([]int, maxSize),
		max:  maxSize,
		ptr:  0,
	}
}

func (this *CustomStack) Push(x int) {
	if this.ptr >= this.max {
		return
	}

	this.data[this.ptr] = x
	this.ptr++
}

func (this *CustomStack) Pop() int {
	if this.ptr <= 0 {
		return -1
	}

	this.ptr--
	item := this.data[this.ptr]
	return item
}

func (this *CustomStack) Increment(k int, val int) {
	for i := 0; i < k && i < this.ptr; i++ {
		this.data[i] += val
	}
}

/**
* Your CustomStack object will be instantiated and called as such:
* obj := Constructor(maxSize);
* obj.Push(x);
* param_2 := obj.Pop();
* obj.Increment(k,val);
 */
