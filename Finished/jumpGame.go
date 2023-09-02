package leetcode

func canJump(nums []int) bool {
	dp := make([]bool, len(nums))
	dp[0] = true
	for i, val := range nums {
		if dp[i] == false {
			continue
		}

		for j := i; j <= i+val; j++ {
			if j >= len(nums) {
				return true
			}
			dp[j] = true
		}
	}

	return dp[len(nums)-1]
}
