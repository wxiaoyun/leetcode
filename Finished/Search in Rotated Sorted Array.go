package leetcode

import "fmt"

func search(nums []int, target int) int {
	pivot := findPivot(nums)

	var low int
	var high int

	// If the pivot index is -1, then the array is not rotated
	// Hence we can search the entire array
	if pivot == -1 {
		low = 0
		high = len(nums) - 1
		// If the target is less than the first element in the array,
		// then the target must be in the right half of the array
	} else if target < nums[0] {
		low = pivot
		high = len(nums) - 1
		// If the target is greater than the first element in the array,
		// then the target must be in the left half of the array
	} else {
		low = 0
		high = pivot - 1
	}

	// Binary search for the target
	for low < high {
		mid := (low + high) / 2

		if nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid
		}
	}

	// Check if the target is at the low index
	if nums[low] == target {
		return low
	}
	return -1
}

// Find the pivot index if it exists, return -1 otherwise
func findPivot(nums []int) int {
	// Since all elements in the array are unique,
	// if the array is rotated, the first element will be greater than the last element.
	// Hence we can do an early return if the first element is less than the last element.
	if nums[0] < nums[len(nums)-1] {
		return -1
	}

	// Binary search for the pivot index
	// The element at the pivot index will be the largest element in the array
	reference := nums[0]

	low := 0
	high := len(nums) - 1

	for low < high {
		mid := (low + high) / 2

		// If the element at the mid index is greater than the reference element,
		// then the pivot index must be to the right of the mid index
		if nums[mid] >= reference {
			low = mid + 1
			// If the element at the mid index is less than the reference element,
			// then the pivot index must be to the left of the mid index
		} else {
			high = mid
		}
	}

	return low
}
