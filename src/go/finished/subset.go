package leetcode

// https://leetcode.com/problems/subsets/

func subsets(nums []int) [][]int {
	res := make([][]int, 0)

	var gen func([]int, int)
	gen = func(accum []int, i int) {
		if i == len(nums) {
			cp := make([]int, len(accum))
			copy(cp, accum)
			res = append(res, cp)
			return
		}

		cp := make([]int, len(accum))
		copy(cp, accum)
		gen(cp, i+1) // No take

		accum = append(accum, nums[i])
		gen(accum, i+1) // take
	}

	gen([]int{}, 0)
	return res
}
