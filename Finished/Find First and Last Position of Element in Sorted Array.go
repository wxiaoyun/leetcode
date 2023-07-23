package leetcode

// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	return []int{findFirst(nums, target), findLast(nums, target)}
}

func findFirst(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l < r {
		mid := (r-l)/2 + l
		if nums[mid] >= target {
			r = mid
		} else {
			l = mid + 1
		}
	}
	if nums[l] == target {
		return l
	}
	return -1
}

func findLast(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l < r {
		mid := (r-l)/2 + l + 1
		if nums[mid] <= target {
			l = mid
		} else {
			r = mid - 1
		}
	}
	if nums[l] == target {
		return l
	}
	return -1
}
