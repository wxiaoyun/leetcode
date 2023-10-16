package leetcode

func lengthOfLIS(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	dp := make([]int, len(nums))

	for i := range dp {
		dp[i] = 1
	}

	max := 1

	for indexRight, right := range nums {
		for indexLeft, left := range nums[:indexRight] {
			if right > left && dp[indexRight] < dp[indexLeft]+1 {
				dp[indexRight] = dp[indexLeft] + 1
				max = maxInt(max, dp[indexRight])
			}
		}
	}

	return max
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
