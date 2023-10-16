package leetcode

// 1,2,3,4,5 -> 1,2,3,5,4
// 1,3,5,2,4 -> 1,3,5,4,2 -> 1,4,2,3,5
// 1,5,3,4,2 -> 1,5,4,3,2 -> 2,1,3,4,5
// 5,1,4,3,2 -> 5,2,1,3,4
func nextPermutation(nums []int) {
	// loop from the end of the array -> find the first value to dip
	// keep track of the current maximum value ecountered so far
	// also keep track of the next larger value
	// swap the dipped value with min value
	// reverse the subarray behind the dipped value
	n := len(nums)
	if n < 2 {
		return
	}

	i := n - 2
	for i >= 0 && nums[i] >= nums[i+1] {
		i--
	}

	if i >= 0 {
		j := n - 1
		for nums[j] <= nums[i] {
			j--
		}
		swapArr(nums, i, j)
	}

	reverseArr(nums, i+1, n-1)
}

func swapArr(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}

func reverseArr(nums []int, start, end int) {
	for start < end {
		swapArr(nums, start, end)
		start++
		end--
	}
}
