package leetcode

// https://leetcode.com/problems/house-robber-ii/

func rob2(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}

	var helper func([]int) int
	helper = func(nums []int) int {
		if len(nums) == 1 {
			return nums[0]
		}

		dp := make([]int, len(nums))
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])

		for i := 2; i < len(nums); i++ {
			dp[i] = max(dp[i-1], nums[i]+dp[i-2])
		}

		return dp[len(nums)-1]
	}

	return max(helper(nums[1:]), helper(nums[:len(nums)-1]))
}

// 2 cases:
// 1. Rob first house, cannot rob last house
// 2. Do not rob first house, can optionally rob last house
