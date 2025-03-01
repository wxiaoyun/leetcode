package leetcode

// Time: O(N)
// Space: O(1)
func longestSubarray(nums []int) int {
	N := len(nums)

	best := 0
	bestVal := 0
	for i := 0; i < N; {
		tmp := nums[i]
		count := 1
		for j := i + 1; j < N && nums[j] == tmp; j++ {
			count++
		}
		if tmp == bestVal {
			best = max(best, count)
		} else if tmp > bestVal {
			best = count
			bestVal = tmp
		}
		i += count
	}

	return best
}

// func max(a, b int) int {
// 	if a > b {
// 		return a
// 	}
// 	return b
// }
