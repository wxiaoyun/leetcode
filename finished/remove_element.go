package leetcode

func removeElement(nums []int, val int) int {
	// initialise two pointers, left and right
	// anything to the left of left is not val
	// anything to the right of right is val
	// anything between left and right is unknown
	left, right := 0, len(nums)-1

	count := 0
	for left <= right {
		for left < len(nums) && nums[left] != val {
			left++
			count++
		}
		// nums[left] now is val
		// need to find a non-val to swap with
		for right >= 0 && nums[right] == val {
			right--
		}

		if left < right {
			// nums[right] now is not val
			// swap
			nums[left], nums[right] = nums[right], nums[left]
		}
		// repeat
	}

	return count
}
