package leetcode

func permute(nums []int) [][]int {
	if len(nums) == 0 {
		return [][]int{{}}
	}

	first := nums[0]
	rest := nums[1:]

	prevPerms := permute(rest)
	var result [][]int

	for _, p := range prevPerms {
		for i := 0; i <= len(p); i++ {
			newPerm := make([]int, len(p)+1)
			copy(newPerm[0:i], p[0:i])
			newPerm[i] = first
			copy(newPerm[i+1:], p[i:])
			result = append(result, newPerm)
		}
	}

	return result
}
