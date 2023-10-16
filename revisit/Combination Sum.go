package leetcode

func combinationSum(candidates []int, target int) [][]int {
	return helper6(candidates, target, []int{}, 0, 0)
}

// Given a combination, return all the correct combinations that sums to target
func helper6(candidates []int, target int, currentCombination []int, curSum int, startIdx int) [][]int {

	// no way the current combinations can sum to the correct combination since each candidate
	// is postive
	if curSum > target {
		return nil
	}

	// just nice we have a combination
	if curSum == target {
		// Create a copy of the current combination and return it
		copyArr := make([]int, len(currentCombination))
		copy(copyArr, currentCombination)
		return [][]int{copyArr}
	}

	solutions := [][]int{}
	// total < target
	// recursively call helper to generate all the combinations
	// for _, num := range candidates {
	// 	solutions = append(solutions, helper(
	// 		candidates, target, append(currentCombination, num), total+num, exists,
	// 	)...)
	// }

	for i := startIdx; i < len(candidates); i++ {
		num := candidates[i]

		newCom := append(currentCombination, num)
		newSum := curSum + num
		solutions = append(solutions, helper6(candidates, target, newCom, newSum, i)...)

	}

	return solutions
}
