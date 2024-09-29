package leetcode

import "math"

type AllOne struct {
	dict   map[string]*dll
	minPtr *dll
	maxPtr *dll
}

type dll struct {
	left  *dll
	right *dll
	key   string
	count int
}

func constructor() AllOne {
	left := &dll{count: 0}
	right := &dll{count: int(math.MaxInt64)}
	left.right = right
	right.left = left
	return AllOne{
		dict:   make(map[string]*dll),
		minPtr: left,
		maxPtr: right,
	}
}

func (this *AllOne) Inc(key string) {
	node, ok := this.dict[key]
	if !ok {
		node = &dll{
			key:   key,
			count: 1,
		}

		this.dict[key] = node
		left := this.minPtr
		right := this.minPtr.right
		left.right = node
		right.left = node
		node.left = left
		node.right = right
		return
	}

	node.count++

	node.left.right = node.right
	node.right.left = node.left

	cur := node.right
	for cur.count < node.count {
		cur = cur.right
	}

	left := cur.left
	right := cur
	left.right = node
	right.left = node
	node.left = left
	node.right = right
}

func (this *AllOne) Dec(key string) {
	node, ok := this.dict[key]
	if !ok {
		panic("Key does not exist")
	}

	node.count--
	if node.count == 0 {
		delete(this.dict, key)

		left := node.left
		right := node.right
		left.right = right
		right.left = left
		node.left = nil
		node.right = nil
		return
	}

	node.left.right = node.right
	node.right.left = node.left

	cur := node.left
	for cur.count > node.count {
		cur = cur.left
	}

	left := cur
	right := cur.right
	left.right = node
	right.left = node
	node.left = left
	node.right = right
}

func (this *AllOne) GetMaxKey() string {
	return this.maxPtr.left.key
}

func (this *AllOne) GetMinKey() string {
	return this.minPtr.right.key
}

/**
* Your AllOne object will be instantiated and called as such:
* obj := Constructor();
* obj.Inc(key);
* obj.Dec(key);
* param_3 := obj.GetMaxKey();
* param_4 := obj.GetMinKey();
 */
