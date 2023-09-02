package leetcode

import "math"

func jump(nums []int) int {
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = math.MaxInt
	}
	dp[0] = 0

	for i, step := range nums {
		for j := i; j <= i+step; j++ {
			if j >= len(nums) {
				break
			}

			dp[j] = min(dp[j], dp[i]+1)
		}
	}

	return dp[len(nums)-1]
}

func min(a, b int) int {
	if a < b {
		return a
	}

	return b
}
