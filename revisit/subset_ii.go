package leetcode

// https://leetcode.com/problems/subsets-ii/

import "sort"

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	res := make([][]int, 0)

	var helper func([]int, int)
	helper = func(accum []int, i int) {
		if i >= len(nums) {
			cp := make([]int, len(accum))
			copy(cp, accum)
			res = append(res, cp)
			return
		}

		helper(append(accum, nums[i]), i+1)
		j := i + 1
		for j < len(nums) && nums[i] == nums[j] {
			j++
		}
		helper(accum, j)
	}

	helper([]int{}, 0)
	return res
}
